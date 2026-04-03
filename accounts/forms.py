from django import forms
from django.contrib.auth.models import User

class AccountSingupForm(forms.Form):
    username = forms.CharField(
        label='Nome de Usuário', 
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control rounded-pill', 'placeholder': 'Ex: felipe_martins'})
    )
    email = forms.EmailField(
        label='E-mail',
        widget=forms.EmailInput(attrs={'class': 'form-control rounded-pill', 'placeholder': 'seu@email.com'})
    )
    CITY_CHOICES = [
        ('', 'Selecione sua cidade'), # Opção vazia inicial
        ('Conceição do Mato dentro', 'Conceição do Mato dentro'),
        ('Gouveia', 'Gouveia'),
        ('Diamantina', 'Diamantina'),
        ('Datas', 'Datas'),
        ('Sabinópolis', 'Sabinópolis'),
        ('Guanhães', 'Guanhães'),
        ('Alvorada de Minas', 'Alvorada de Minas'),
        ('Cantagalo', 'Cantagalo'),
        ('Peçanha', 'Peçanha'),
        ('Presidente Kubitschek', 'Presidente Kubitschek'),
        ('Santo Antônio do Itambé', 'Santo Antônio do Itambé'),
        ('Serra Azul', 'Serra Azul'),
        ('Serro', 'Serro'),
    ]
    
    city = forms.ChoiceField(
        label='Cidade',
        choices=CITY_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select rounded-pill'})
    )

    # Validação e-mail
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este e-mail já está cadastrado.")
        return email
    
    # class Meta:
    #     model = User
    #     fields = ['username', 'email', 'city', 'password']
    #     widgets = {
    #         'city': forms.Select(choices=[
    #             (1, 'Conceição do Mato dentro'),
    #             (2, 'Gouveia'),
    #             (3, 'Diamantina'),
    #             (4, 'Datas'),
    #             (5, 'Sabinópolis'),
    #             (6, 'Guanhães'),
    #             (7, 'Alvorada de Minas'),
    #             (8, 'Cantagalo'),
    #             (9, 'Peçanha'),
    #             (10, 'Presidente Kubitschek'),
    #             (11, 'Santo Antônio do Itambé'),
    #             (12, 'Serra Azul'),
    #             (13, 'Serro')
    #         ])
    #     }
