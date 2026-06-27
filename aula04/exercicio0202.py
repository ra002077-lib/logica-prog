grupo1 = {}
grupo2 = {}
grupo3 = {}


qtd1 = int(input("Quantos produtos no grupo ELETRODOMESTICOS? "))
for i in range(qtd1):
    item = input(f"Digite o nome do {i+1}° item: ")
    grupo1.append(item)
print("--- COMBINAÇÕES GERADAS ---")
contador = 0

qtd2 = int(input("Quantos produtos no grupo COMIDAS? "))
for i in range(qtd2):
    item = input(f"Digite o nome do {i+1}° item: ")
    grupo2.append(item)
print("--- COMBINAÇÕES GERADAS ---")
contador = 0

qtd3 = int(input("Quantos produtos no grupo UTILIDADES? "))
for i in range(qtd3):
    item = input(f"Digite o nome do {i+1}° item: ")
    grupo3.append(item)
print("--- COMBINAÇÕES GERADAS ---")
contador = 0

for a in grupo1:
    for b in grupo2:
        for c in grupo3:
            if (a != b) and (b != c) and (a != c):
                print(f'{a} + {b} + {c}')
print(f'Foram um total de {contador} combinações: ')