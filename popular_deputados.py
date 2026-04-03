import os
import django
from django.core.files import File

# 1. Configuração do ambiente Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webEnquete.settings') # Ajuste o nome do seu projeto
django.setup()

from polls.models import Deputado # Ajuste o nome do seu app

def popular_deputados():
    # Caminho onde as fotos originais estão guardadas (backup)
    CAMINHO_FOTOS_LOCAL = './fotos_originais/' 

    # Lista de deputados extraída do seu documento de afinidades 
    # Adicionei os partidos mais comuns de cada um para facilitar
    deputados_dados = [
        {"nome": "Amanda Teixeira Dias", "partido": "PL", "arquivo": "amanda_teixeira.jpg"},
        {"nome": "Ana Paula Siqueira", "partido": "REDE", "arquivo": "ana_paula_siqueira.jpg"},
        {"nome": "Andréia de Jesus", "partido": "PT", "arquivo": "andreia_jesus.jpg"},
        {"nome": "Bella Gonçalves", "partido": "PSOL", "arquivo": "bella_goncalves.jpg"},
        {"nome": "Bosco", "partido": "CIDADANIA", "arquivo": "bosco.jpg"},
        {"nome": "Carlos Pimenta", "partido": "PDT", "arquivo": "carlos_pimenta.jpg"},
        {"nome": "Carol Caram", "partido": "AVANTE", "arquivo": "carol_caram.jpg"},
        {"nome": "Dr Mauricio", "partido": "NOVO", "arquivo": "dr_mauricio.jpg"},
        {"nome": "Grego da Fundação", "partido": "MOBILIZA", "arquivo": "grego_fundacao.jpg"},
        {"nome": "Ioni Pinheiro", "partido": "UNIÃO", "arquivo": "ioni_pinheiro.jpg"},
        {"nome": "Leandro Genaro", "partido": "PSD", "arquivo": "leandro_genaro.jpg"},
        {"nome": "Lohanna", "partido": "PV", "arquivo": "lohanna.jpg"},
        {"nome": "Lud Falcão", "partido": "PODEMOS", "arquivo": "lud_falcao.jpg"},
        {"nome": "Maria Clara Marra", "partido": "PCdoB", "arquivo": "maria_clara_marra.jpg"},
        {"nome": "Mauro Tramonte", "partido": "REPUBLICANOS", "arquivo": "mauro_tramonte.jpg"},
        {"nome": "Nayara Rocha", "partido": "PP", "arquivo": "nayara_rocha.jpg"},
        {"nome": "Neilando Pimenta", "partido": "PSB", "arquivo": "neilando_pimenta.jpg"},
        {"nome": "Roberto Andrade", "partido": "PRD", "arquivo": "roberto_andrade.jpg"},
        {"nome": "Tadeu Leite", "partido": "MDB", "arquivo": "tadeu_leite.jpg"},
        {"nome": "Prof. Wendel Mesquita", "partido": "SOLIDARIEDADE", "arquivo": "wendel_mesquita.jpg"},
    ]

    print("Iniciando a criação de deputados...")

    for dados in deputados_dados:
        # get_or_create: busca pelo nome, se não existir, cria com o partido
        deputado, criado = Deputado.objects.get_or_create(
            name=dados["nome"],
            defaults={'partido': dados["partido"]}
        )

        if criado:
            caminho_arquivo = os.path.join(CAMINHO_FOTOS_LOCAL, dados["arquivo"])
            
            if os.path.exists(caminho_arquivo):
                with open(caminho_arquivo, 'rb') as f:
                    # O Django copiará o arquivo para public/deputados/
                    deputado.imagem.save(dados["arquivo"], File(f), save=True)
                print(f"✅ Criado: {dados['nome']} - {dados['partido']}")
            else:
                print(f"⚠️ Criado: {dados['nome']}, mas a foto '{dados['arquivo']}' não foi encontrada.")
        else:
            print(f"ℹ️ {dados['nome']} já existe no sistema.")

if __name__ == "__main__":
    popular_deputados()