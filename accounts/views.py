from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.views.generic import TemplateView

from django.contrib.auth import get_user_model
User = get_user_model()

from accounts.forms import AccountSingupForm
from polls.models import QuestionUser

# Create your views here.

class AccountCreateView(CreateView):
    model = User
    template_name = 'registration/signup_form.html'
    form_class = AccountSingupForm
    success_url = reverse_lazy('login')
    success_message = "Usuário criado com sucesso!"
    
    def form_valid(self, form) -> HttpResponse:
        form.instance.password = make_password(form.instance.password)
        form.save()
        messages.success(self.request, self.success_message)
        return super(AccountCreateView, self).form_valid(form)

class AccountTemplateView(TemplateView):
    template_name = 'account/user_detail.html'
    content_object_name = 'user'
    
    def get_context_data(self, **kwargs):
        context = super(AccountTemplateView, self).get_context_data(**kwargs)
        voted = QuestionUser.objects.filter(user=self.request.user)
        context['questions_voted'] = voted
        return context