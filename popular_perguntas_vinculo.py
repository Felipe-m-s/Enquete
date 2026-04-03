import os
import django
from django.utils import timezone

# 1. Configuração do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webEnquete.settings')
django.setup()

from polls.models import Question, Choice, Deputado

def relacionar():
    print("--- Iniciando a criação de Choices e Vinculação ---")

    def criar_choice_e_vincular(id_da_pergunta, texto_da_escolha, lista_nomes):
        try:
            # 1. Buscamos a Pergunta "pai"
            pergunta = Question.objects.get(pk=id_da_pergunta)
            
            # 2. Criamos a Alternativa (Choice) para essa pergunta
            # get_or_create evita duplicados se você rodar o script de novo
            alternativa, criada = Choice.objects.get_or_create(
                question=pergunta,
                choice_text=texto_da_escolha
            )
            
            # 3. Buscamos os deputados pelos nomes fornecidos
            deputados = Deputado.objects.filter(name__in=lista_nomes)
            
            # 4. Adicionamos a relação Many-to-Many
            # IMPORTANTE: Verifique se no seu model Choice o campo é 'deputados_relacionados' ou 'deputado_relacionado'
            alternativa.deputados_relacionados.add(*deputados)
            
            status = "Criada" if criada else "Atualizada"
            print(f"✅ {status}: '{texto_da_escolha}' na Questão {id_da_pergunta}. Vinculados {deputados.count()} deputados.")
            
        except Question.DoesNotExist:
            print(f"❌ Erro: Não existe Pergunta com o ID {id_da_pergunta}.")
        except Exception as e:
            print(f"⚠️ Erro inesperado: {e}")

    # --- MAPEAMENTO ---
    # Estrutura: criar_choice_e_vincular(ID_DA_QUESTÃO, "TEXTO DA ESCOLHA", ["LISTA DE DEPUTADOS"])
    
    # Exemplo Pergunta 1
    criar_choice_e_vincular(1, "Em hospitais e centros especializados para pessoas com deficiência", ["Andréia de Jesus", "Mauro Tramonte", "Maria Clara Marra"])
    criar_choice_e_vincular(1, "Escolas e programas de primeiro emprego para jovens", ["Carlos Pimenta", "Maria Clara Marra", "Prof. Wendel Mesquita", "Bosco"])
    criar_choice_e_vincular(1, "Obras na cidade", ["Roberto Andrade", "Leandro Genaro", "Nayara Rocha", "Carol Caram", "Dr Mauricio", 
                                "Ioni Pinheiro", "Tadeu Leite"])
    criar_choice_e_vincular(2, "Preços abusivos", ["Andréia de Jesus", "Dr Mauricio", "Lud Falcão"])
    criar_choice_e_vincular(2, "Falta de segurança pública", ["Amanda Teixeira Dias", "Mauro Tramonte", "Nayara Rocha", "Carlos Pimenta"])
    criar_choice_e_vincular(2, "Falta de valorização da cultura regional", ["Bella Gonçalves", "Ana Paula Siqueira", "Lohanna", "Grego da Fundação"])
    criar_choice_e_vincular(3, "Comunidades tradicionais e quilombolas", ["Bella Gonçalves", "Ana Paula Siqueira", "Grego da Fundação"])
    criar_choice_e_vincular(3, "Mulheres em situação de vulnerabilidade", ["Andréia de Jesus", "Maria Clara Marra", "Bosco"])
    criar_choice_e_vincular(3, "Idosos e aposentados", ["Mauro Tramonte", "Nayara Rocha", "Tadeu Leite", "Roberto Andrade"])
    criar_choice_e_vincular(4, "Focada em direitos humanos e justiça social", ["Bella Gonçalves", "Andréia de Jesus", "Bosco"])
    criar_choice_e_vincular(4, "Boa administração da verba pública", ["Leandro Genaro", "Tadeu Leite", "Ioni Pinheiro", "Nayara Rocha"])
    criar_choice_e_vincular(4, "Focada no desenvolvimento de pequenas comunidades", ["Grego da Fundação", "Mauro Tramonte", "Ana Paula Siqueira"])
    criar_choice_e_vincular(5, "Inclusão de pessoas com deficiência", ["Andréia de Jesus", "Maria Clara Marra"])
    criar_choice_e_vincular(5, "Proteção do meio ambiente", ["Ana Paula Siqueira", "Lohanna"])
    criar_choice_e_vincular(5, "Fortalecimento da família e políticas para a infância", ["Amanda Teixeira Dias", "Mauro Tramonte", "Carlos Pimenta"])
    criar_choice_e_vincular(6, "Maiores oportunidades de emprego", ["Dr Mauricio", "Leandro Genaro", "Prof. Wendel Mesquita"])
    criar_choice_e_vincular(6, "Melhor qualidade da saúde pública", ["Mauro Tramonte", "Andréia de Jesus"])
    criar_choice_e_vincular(6, "Investimentos na educação", ["Carlos Pimenta", "Bosco", "Maria Clara Marra"])
    criar_choice_e_vincular(7, "Combate à corrupção", ["Lud Falcão", "Dr Mauricio"])
    criar_choice_e_vincular(7, "Redução da pobreza", ["Andréia de Jesus", "Bella Gonçalves"])
    criar_choice_e_vincular(7, "Geração de empregos", ["Prof. Wendel Mesquita", "Leandro Genaro"])
    criar_choice_e_vincular(8, "Incentivar o comércio local", ["Dr Mauricio", "Nayara Rocha", "Roberto Andrade"])
    criar_choice_e_vincular(8, "Mais espaços de cultura e lazer", ["Bella Gonçalves", "Lohanna", "Grego da Fundação"])
    criar_choice_e_vincular(8, "Investimentos em cursos profissionalizantes para a população", ["Carlos Pimenta", "Maria Clara Marra", "Prof. Wendel Mesquita"])
    criar_choice_e_vincular(9, "Violência", ["Amanda Teixeira Dias", "Mauro Tramonte"])
    criar_choice_e_vincular(9, "Desemprego", ["Prof. Wendel Mesquita", "Andréia de Jesus"])
    criar_choice_e_vincular(9, "Falta de infraestrutura", ["Nayara Rocha", "Tadeu Leite", "Leandro Genaro"])
    criar_choice_e_vincular(10, "Participação ativa dos cidadãos nas decisões públicas", ["Bella Gonçalves", "Grego da Fundação", "Bosco"])
    criar_choice_e_vincular(10, "Incentivo ao voluntariado e ações sociais", ["Mauro Tramonte", "Prof. Wendel Mesquita"])
    criar_choice_e_vincular(10, "Mais investimentos públicos", ["Andréia de Jesus", "Leandro Genaro"])
    criar_choice_e_vincular(11, "Melhor iluminação pública", ["Amanda Teixeira Dias"])
    criar_choice_e_vincular(11, "Mais áreas de lazer e praças", ["Bella Gonçalves", "Lohanna"])
    criar_choice_e_vincular(11, "Melhor transporte público", ["Carlos Pimenta", "Maria Clara Marra"])
    criar_choice_e_vincular(11, "Melhor infraestrutura", ["Nayara Rocha", "Tadeu Leite", "Roberto Andrade"])
    criar_choice_e_vincular(12, "Programas de esporte", ["Mauro Tramonte"])
    criar_choice_e_vincular(12, "Cursos de capacitação profissional", ["Carlos Pimenta", "Maria Clara Marra"])
    criar_choice_e_vincular(12, "Projetos culturais e artísticos", ["Bella Gonçalves", "Grego da Fundação"])
    criar_choice_e_vincular(12, "Oportunidade de emprego", ["Dr Mauricio", "Prof. Wendel Mesquita"])
    criar_choice_e_vincular(13, "Incentivo a candidaturas femininas", ["Andréia de Jesus"])
    criar_choice_e_vincular(13, "Programas de formação política para mulheres", ["Maria Clara Marra"])
    criar_choice_e_vincular(13, "Campanhas de conscientização sobre igualdade de gênero", ["Bella Gonçalves", "Ana Paula Siqueira"])
    criar_choice_e_vincular(13, "Maior apoio institucional dentro dos partidos", ["Tadeu Leite", "Nayara Rocha"])
    criar_choice_e_vincular(14, "Criação de campanhas de conscientização sobre cuidados com animais", ["Ana Paula Siqueira"])
    criar_choice_e_vincular(14, "Fiscalização mais rigorosa contra maus-tratos", ["Nayara Rocha", "Amanda Teixeira Dias"])
    criar_choice_e_vincular(14, "Apoio a ONGs e abrigos de proteção animal", ["Bella Gonçalves"])
    criar_choice_e_vincular(14, "Programas de adoção responsável", ["Lohanna", "Mauro Tramonte"])
    criar_choice_e_vincular(14, "Minha cidade não enfrenta problema com maus-tratos aos animais", [])
    criar_choice_e_vincular(15, "Ampliação do atendimento nos postos de saúde", ["Andréia de Jesus"])
    criar_choice_e_vincular(15, "Mais médicos e profissionais de saúde", ["Maria Clara Marra", "Carlos Pimenta"])
    criar_choice_e_vincular(15, "Investimento em hospitais e equipamentos", ["Nayara Rocha", "Tadeu Leite"])
    criar_choice_e_vincular(15, "Programas de prevenção e campanhas de saúde", ["Ana Paula Siqueira", "Lohanna"])
    
    print("--- Processo concluído ---")

if __name__ == "__main__":
    relacionar()