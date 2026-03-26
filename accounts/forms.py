from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()

class AccountSingupForm(forms.ModelForm):
    password = forms.CharField(label='Senha', max_length=50, widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ['username', 'email', 'city', 'password']
        widgets = {
            'city': forms.Select(choices=[
                (1, 'Conceição do Mato dentro'),
                (2, 'Gouveia'),
                (3, 'Diamantina'),
                (4, 'Datas'),
                (5, 'Sabinópolis'),
                (6, 'Guanhães'),
                (7, 'Alvorada de Minas'),
                (8, 'Cantagalo'),
                (9, 'Peçanha'),
                (10, 'Presidente Kubitschek'),
                (11, 'Santo Antônio do Itambé'),
                (12, 'Serra Azul'),
                (13, 'Serro')
            ])
        }
