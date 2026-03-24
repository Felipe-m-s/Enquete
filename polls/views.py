from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.http import HttpResponse
from django.contrib import messages

from polls.models import Question

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

