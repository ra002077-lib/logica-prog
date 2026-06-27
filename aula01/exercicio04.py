# Peça ao usuario para inserir 2 tipos de frutas e 2 tipos de bebidas. Apos preencher as duas listas, o programa deve cruzar os dados e exibir as combinações, exceto se a fruta for manga, e a bebida for leite.

frutas = []
bebidas = []

for i in range(2):
    frutas.append(input(f"Digite a {i+i}° fruta:"))

for i in range(2):
    bebidas.append(input(f"Digite a {i+i}° bebida: "))
print("--- Kits Alimentícios identificados ---")
for f in frutas:
    for b in bebidas:
        if not (f"" == "manga" and b == "leite"):
            print(f"Combinação: {f} com {b}")
        else:
            print(f"Combinação: {f} + {b} **** inválida! ****")




