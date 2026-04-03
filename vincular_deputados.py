import os
import django

# 1. Configuração do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webEnquete.settings')
django.setup()

from polls.models import Choice, Deputado

def relacionar():
    print("--- Iniciando a vinculação por ID (PK) ---")

    def adicionar_vinculo_por_id(id_da_escolha, lista_nomes):
        try:
            # Buscamos pela Primary Key (pk) ou id
            alternativa = Choice.objects.get(pk=id_da_escolha) 
            
            # Buscamos os deputados [cite: 1-26]
            deputados = Deputado.objects.filter(name__in=lista_nomes)
            
            # Adicionamos a relação
            alternativa.deputados_relacionados.add(*deputados)
            print(f"✅ Sucesso: Escolha ID {id_da_escolha} vinculada a {deputados.count()} deputados.")
            
        except Choice.DoesNotExist:
            print(f"❌ Erro: Não existe Choice com o ID {id_da_escolha}.")

    # --- MAPEAMENTO ---
    # Exemplo: Supondo que a alternativa de saúde seja o ID 1
    adicionar_vinculo_por_id(1, ["Andréia de Jesus", "Mauro Tramonte", "Maria Clara Marra"])
    
    # Exemplo: Supondo que a alternativa de segurança seja o ID 2
    adicionar_vinculo_por_id(2, ["Carlos Pimenta", "Maria Clara Marra", "Prof. Wendel Mesquita", "Bosco"])
    adicionar_vinculo_por_id(3, ["Roberto Andrade", "Leandro Genaro", "Nayara Rocha", "Carol Caram", "Dr Mauricio", 
                                "Ioni Pinheiro", "Tadeu Leite"])
    adicionar_vinculo_por_id(4, ["Andréia de Jesus", "Dr Mauricio", "Lud Falcão"])
    adicionar_vinculo_por_id(5, ["Amanda Teixeira Dias", "Mauro Tramonte", "Nayara Rocha", "Carlos Pimenta"])
    adicionar_vinculo_por_id(6, ["Bella Gonçalves", "Ana Paula Siqueira", "Lohanna", "Grego da Fundação"])
    adicionar_vinculo_por_id(7, ["Bella Gonçalves", "Ana Paula Siqueira", "Grego da Fundação"])
    adicionar_vinculo_por_id(8, ["Andréia de Jesus", "Maria Clara Marra", "Bosco"])
    adicionar_vinculo_por_id(9, ["Mauro Tramonte", "Nayara Rocha", "Tadeu Leite", "Roberto Andrade"])
    adicionar_vinculo_por_id(10, ["Bella Gonçalves", "Andréia de Jesus", "Bosco"])
    adicionar_vinculo_por_id(11, ["Leandro Genaro", "Tadeu Leite", "Ioni Pinheiro", "Nayara Rocha"])
    adicionar_vinculo_por_id(12, ["Grego da Fundação", "Mauro Tramonte", "Ana Paula Siqueira"])
    adicionar_vinculo_por_id(13, ["Andréia de Jesus", "Maria Clara Marra"])
    adicionar_vinculo_por_id(14, ["Ana Paula Siqueira", "Lohanna"])
    adicionar_vinculo_por_id(15, ["Amanda Teixeira Dias", "Mauro Tramonte", "Carlos Pimenta"])
    adicionar_vinculo_por_id(16, ["Dr Mauricio", "Leandro Genaro", "Prof. Wendel Mesquita"])
    adicionar_vinculo_por_id(17, ["Mauro Tramonte", "Andréia de Jesus"])
    adicionar_vinculo_por_id(18, ["Carlos Pimenta", "Bosco", "Maria Clara Marra"])
    adicionar_vinculo_por_id(19, ["Lud Falcão", "Dr Mauricio"])
    adicionar_vinculo_por_id(20, ["Andréia de Jesus", "Bella Gonçalves"])
    adicionar_vinculo_por_id(21, ["Prof. Wendel Mesquita", "Leandro Genaro"])
    adicionar_vinculo_por_id(22, ["Dr Mauricio", "Nayara Rocha", "Roberto Andrade"])
    adicionar_vinculo_por_id(23, ["Bella Gonçalves", "Lohanna", "Grego da Fundação"])
    adicionar_vinculo_por_id(24, ["Carlos Pimenta", "Maria Clara Marra", "Prof. Wendel Mesquita"])
    adicionar_vinculo_por_id(25, ["Amanda Teixeira Dias", "Mauro Tramonte"])
    adicionar_vinculo_por_id(26, ["Prof. Wendel Mesquita", "Andréia de Jesus"])
    adicionar_vinculo_por_id(27, ["Nayara Rocha", "Tadeu Leite", "Leandro Genaro"])
    adicionar_vinculo_por_id(28, ["Bella Gonçalves", "Grego da Fundação", "Bosco"])
    adicionar_vinculo_por_id(29, ["Mauro Tramonte", "Prof. Wendel Mesquita"])
    adicionar_vinculo_por_id(30, ["Andréia de Jesus", "Leandro Genaro"])
    adicionar_vinculo_por_id(31, ["Amanda Teixeira Dias"])
    adicionar_vinculo_por_id(32, ["Bella Gonçalves", "Lohanna"])
    adicionar_vinculo_por_id(33, ["Carlos Pimenta", "Maria Clara Marra"])
    adicionar_vinculo_por_id(34, ["Nayara Rocha", "Tadeu Leite", "Roberto Andrade"])
    adicionar_vinculo_por_id(35, ["Mauro Tramonte"])
    adicionar_vinculo_por_id(36, ["Carlos Pimenta", "Maria Clara Marra"])
    adicionar_vinculo_por_id(37, ["Bella Gonçalves", "Grego da Fundação"])
    adicionar_vinculo_por_id(38, ["Dr Mauricio", "Prof. Wendel Mesquita"])
    adicionar_vinculo_por_id(39, ["Andréia de Jesus"])
    adicionar_vinculo_por_id(40, ["Maria Clara Marra"])
    adicionar_vinculo_por_id(41, ["Bella Gonçalves", "Ana Paula Siqueira"])
    adicionar_vinculo_por_id(42, ["Tadeu Leite", "Nayara Rocha"])
    adicionar_vinculo_por_id(43, ["Ana Paula Siqueira"])
    adicionar_vinculo_por_id(44, ["Nayara Rocha", "Amanda Teixeira Dias"])
    adicionar_vinculo_por_id(45, ["Bella Gonçalves"])
    adicionar_vinculo_por_id(46, ["Lohanna", "Mauro Tramonte"])
    adicionar_vinculo_por_id(47, ["Andréia de Jesus"])
    adicionar_vinculo_por_id(48, ["Maria Clara Marra", "Carlos Pimenta"])
    adicionar_vinculo_por_id(49, ["Nayara Rocha", "Tadeu Leite"])
    adicionar_vinculo_por_id(50, ["Ana Paula Siqueira", "Lohanna"])

    print("--- Processo concluído ---")

if __name__ == "__main__":
    relacionar()