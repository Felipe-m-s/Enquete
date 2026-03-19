from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    # return HttpResponse("Olá")
    # return render(request, 'index.html')
    return render (request, 'index.html', {'title': 'Bem-vindo à Enquete!'})


