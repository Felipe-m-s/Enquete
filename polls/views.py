from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from django.urls import reverse_lazy
from polls.models import Question, Choice
from django.views.generic import DetailView, ListView
from django.core.exceptions import ValidationError

from django.contrib.auth import get_user_model
User = get_user_model()


# Create your views here.

def index(request):
    # return HttpResponse("Olá")
    # return render(request, 'index.html')
    aviso = 'Aviso importante: Esta pagina não precisa de login para ser acessada.'
    messages.warning(request, aviso)
    return render (request, 'index.html', {'title': 'Bem-vindo à Enquete!'})

@login_required
def ola(request):
    questions = Question.objects.all()
    context = {
        'all_question': questions
    }
    return render(request, 'polls/questions.html', context)

class QuestionDetailView(DetailView):
    model = Question
    template_name = 'polls/question_detail.html'
    context_object_name = 'question'
    
    def get_context_data(self, **kwargs):
        context = super(QuestionDetailView, self).get_context_data(**kwargs)
        return context

class QuestionListView(ListView):
    model = Question
    template_name = 'polls/question_list.html'
    context_object_name = 'questions'

@login_required
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        try:
            selected_choice = question.choice_set.get(pk=request.POST['choice'])
            session_user = get_object_or_404(User, id=request.user.id)
            selected_choice.votes += 1
            selected_choice.save(user=session_user)
        except (KeyError, Choice.DoesNotExist):
            messages.error(request, "Selecione uma alternativa válida.")
        except (ValidationError) as e:
            messages.error(request, e.message)
        else:
            messages.success(request, "Voto registrado com sucesso!")
            return redirect(reverse_lazy('question_detail', args=(question.id,)))
        
    context = {'question': question,}
    return render(request, 'polls/question_detail.html', context)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question,}
    context['votes'] = question.get_results()
    
    return render(request, 'polls/results.html', context)