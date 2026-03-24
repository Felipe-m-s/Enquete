from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from polls.models import Question

def index(request):
    # return HttpResponse("Olá")
    # return render(request, 'index.html')
    return render (request, 'index.html', {'title': 'Bem-vindo à Enquete!'})

@login_required
def ola(request):
    questions = Question.objects.all()
    context = {
        'all_question': questions
    }
    return render(request, 'polls/questions.html', context)

