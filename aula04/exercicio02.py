import itertools

def coletar_itens(nome_grupo):
    print(f"\n--- Configuração do Grupo: {nome_grupo} ---")
    while True:
        try:
            qtd = int(input(f"Quantos produtos haverá no grupo {nome_grupo}? "))
            if qtd <= 0:
                print("Por favor, insira um número maior que zero.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

    itens = set() # Usamos set para evitar nomes duplicados dentro do mesmo grupo
    for i in range(qtd):
        item = input(f"Digite o nome do {i+1}º item: ").strip().capitalize()
        itens.add(item)
    
    return list(itens)

def main():
    print("=== SISTEMA DE PROMOÇÃO - LOJA (80% DE DESCONTO) ===")
    
    # Coleta de dados dos grupos
    grupo_eletro = coletar_itens("ELETRODOMÉSTICO (Grupo 1)")
    grupo_comida = coletar_itens("COMIDAS (Grupo 2)")
    grupo_utilid = coletar_itens("UTILIDADES (Grupo 3)")

    # Gerar o produto cartesiano entre os três grupos
    # Isso garante 1 item de cada grupo em todas as variações possíveis
    combinacoes = list(itertools.product(grupo_eletro, grupo_comida, grupo_utilid))

    # Filtrar combinações onde não existam nomes iguais entre grupos diferentes
    # (Ex: se "Copo" estivesse em Comidas e Utilidades ao mesmo tempo)
    combinacoes_validas = [
        c for c in combinacoes if len(set(c)) == 3
    ]

    print("\n" + "="*50)
    print(f"PROMOÇÃO ATIVA: Compre 3 itens (1 de cada grupo) e ganhe 80% OFF!")
    print(f"Total de combinações possíveis: {len(combinacoes_validas)}")
    print("="*50)

    for idx, combo in enumerate(combinacoes_validas, 1):
        print(f"Sugestão {idx}: {combo} + {combo} + {combo}")

if __name__ == "__main__":
    main()
