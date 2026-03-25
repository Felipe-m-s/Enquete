from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from polls.models import Question
from django.views.generic import DetailView, ListView


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

class QuestionListView(ListView):
    model = Question
    template_name = 'polls/question_list.html'
    context_object_name = 'questions'