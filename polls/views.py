from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from django.urls import reverse_lazy
from polls.models import Question, Choice, Deputado, QuestionUser
from django.views.generic import DetailView, ListView
from django.core.exceptions import ValidationError
from collections import Counter


from django.contrib.auth import get_user_model
User = get_user_model()


# Create your views here.

def index(request):
    return render (request, 'core/index.html', {'title': 'Bem-vindo à enquete da Semana Jurídica!'})

@login_required
def home(request):
    # Obtendo o user_name do usuário logado
    user_name = request.user.username
    
    # Obtendo a cidade do perfil do usuário logado
    city = request.user.profile.city
    
    # Verificando se o usuário já respondeu a alguma questão
    ansered_questions = QuestionUser.objects.filter(user=request.user).exists()
    
    # Formatando o user_name para exibição (removendo underscores e capitalizando)
    user_name = user_name.replace('_', ' ').title()
    
    context = {
        'user_name': user_name,
        'city': city,
        'ansered_questions': ansered_questions
    }
    return render(request, 'core/home.html', context)

def about(request):
    return render(request, 'core/about.html')

class QuestionListView(ListView):
    model = Question
    template_name = 'polls/question_list.html'
    context_object_name = 'questions'

# Função para obter a próxima questão
def get_next_question(current_question):
    return Question.objects.filter(id__gt=current_question.id).order_by('id').first()

@login_required
def vote(request, question_id):
    # Busca a questão atual
    question = get_object_or_404(Question, pk=question_id)
    
    # Pega o id da próxima questão
    next_question = get_next_question(question)
    # Variável para verificar se a questão atual é a última
    is_last_question = not next_question
    
    # Cálculo de progresso
    amount_questions = Question.objects.count()
    current_position = Question.objects.filter(id__lte=question.id).count()
    progress = (float(current_position) / float(amount_questions)) * 100 if amount_questions > 0 else 0
    
    if request.method == 'POST':
        try:
            # Busca a escolha selecionada pelo usuário
            selected_choice = question.choice_set.get(pk=request.POST['choice'])
            
            # Salva ou atualiza a resposta do usuário para a questão atual
            created = QuestionUser.objects.update_or_create(
                user = request.user,
                question = question,
                defaults={'choice': selected_choice}
            )
            
            # Se a resposta foi criada, exibe mensagem de sucesso.
            # Se foi atualizada, exibe mensagem de atualização.
            if created:
                messages.success(request, "Resposta salva com sucesso!")
            else:
                messages.success(request, "Resposta atualizada com sucesso!")
            
            
            # Redireciona para a próxima questão ou para os resultados se for a última
            if next_question:
                return redirect('question_detail', question_id=next_question.id)
            else:
                return redirect('poll_results_match')
        
        # Tratamento de exceções para escolha inválida
        except (KeyError, Choice.DoesNotExist):
            messages.error(request, "Selecione uma alternativa válida.")
            return redirect('question_detail', pk=question.id)
        except (ValidationError) as e:
            messages.error(request, e.message)

    # Contexto para renderizar a questão atual e o progresso
    context = {'question': question,
                'progress': progress,
                'is_last_question': is_last_question,
                'position': current_position,
                'amount_questions': amount_questions}
    return render(request, 'polls/question_detail.html', context)

@login_required
def results_match(request):
    
    # Obter os votos do usuário
    user_votes = QuestionUser.objects.filter(user=request.user).select_related('choice')
    amount_votes = user_votes.count()
    counter = Counter()
    
    # Percorrer os votos do usuário e contar os deputados associados às escolhas
    for vote in user_votes:
        if vote.choice:
            deputados = vote.choice.deputados_relacionados.all()
            counter.update(deputados)
    
    # Criar o ranking dos deputados com contagem e porcentagem
    ranking = []
    for deputado, count in counter.most_common(3):  # Exibir apenas os 3 mais votados
        ranking.append({
            'deputado': deputado,
            'count': count,
            'percentage': (count / amount_votes) * 100 if amount_votes > 0 else 0
        })
    
    return render(request, 'polls/results_match.html', {'matches': ranking})
