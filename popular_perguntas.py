import os
import django
from django.utils import timezone # Importante para o campo pub_date

# 1. Configuração do ambiente Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webEnquete.settings')
django.setup()

from polls.models import Question

def popular_perguntas():
    # Sua lista de perguntas para a Semana Jurídica
    perguntas = [
        "Se sua cidade tivesse uma verba extra, onde você gostaria que fosse investido?",
        "Quais desses problemas mais te afeta no dia a dia?",
        "Qual grupo social é mais negligenciado na sua cidade?",
        "Qual sua definição de uma boa gestão pública?",
        "Se um projeto de lei fosse sugerido hoje, em qual você votaria?",
        "Qual mudança você espera ver nos próximos anos?",
        "Qual você considera uma prioridade hoje?",
        "O que mais ajudaria no desenvolvimento da sua cidade?",
        "Qual desses problemas você considera mais urgente resolver?",
        "Qual dessas atitudes ajudam a melhorar a sociedade?",
        "Qual dessas melhorias faria mais diferença no seu bairro?",
        "Qual dessas iniciativas ajudaria mais os jovens da cidade?",
        "O que poderia ajudar a aumentar a participação das mulheres na política em sua cidade?",
        "Sua cidade enfrenta problemas com maus-tratos aos animais? Se sim, qual dessas ações poderia melhorar a proteção dos animais?",
        "O que poderia melhorar a qualidade da saúde pública em sua cidade?",
    ]

    print("--- Iniciando a criação de perguntas ---")

    for texto in perguntas:
        # get_or_create busca pelo texto. 
        # Se não existir, cria usando os dados do 'defaults'
        obj, criado = Question.objects.get_or_create(
            question_text=texto,
            defaults={'pub_date': timezone.now()} # Preenche com a data/hora atual
        )

        if criado:
            print(f"✅ Criada: {texto}")
        else:
            print(f"ℹ️ Já existia: {texto}")

    print("--- Finalizado! ---")

if __name__ == "__main__":
    popular_perguntas()