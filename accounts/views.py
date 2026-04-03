from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import TemplateView
from django.contrib.auth import get_user_model, login
import uuid

User = get_user_model()

from accounts.forms import AccountSingupForm
from accounts.models import UserProfile
from polls.models import QuestionUser

# Create your views here.

class AccountCreateView(FormView):
    template_name = 'registration/signup_form.html'
    form_class = AccountSingupForm
    success_url = reverse_lazy('ola')
    
    def form_valid(self, form) -> HttpResponse:
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        city = form.cleaned_data['city']
        
        user = User.objects.filter(username=username).first()
        
        if not user:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=str(uuid.uuid4().hex)  # Gerar uma senha aleatória
            )
            UserProfile.objects.create(user=user, city=city)
            messages.success(self.request, "Bem-vindo! Cadastro realizado com sucesso.")
        else:
            messages.info(self.request, "Bem-vindo de volta!")

        login(self.request, user)  # Logar o usuário após a criação da conta
        
        return redirect(self.success_url)

class AccountTemplateView(TemplateView):
    template_name = 'account/user_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            voted = QuestionUser.objects.filter(user=self.request.user)
            context['questions_voted'] = voted
            try:
                context['profile'] = self.request.user.username
            except:
                context['profile'] = None
        return context