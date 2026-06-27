# Crie um código que:
# - receba 5 itens
# - faça a ordenação da lista
# - exiba a lista ordenada
# - crie uma segunda lista que contenha a lista invertida.


meus_itens = []                            # lista precisa ser declarada inicialmente para uso.

for i in range(1,6):                    # faz a contagem de 1 a 5
    item = input(f'Digite o item {i}: ')  # input de item
    meus_itens.append(item)              # adiciona item ao final da lista

meus_itens.sort()                        # faz a ordenação definitiva da lista
print(meus_itens)                        # exibe a lista em ordem alfabética

# criando uma segunda lista com os itens organizados na ordem alfabética invertida
meus_itens_invertido=sorted(meus_itens, reverse=True)
print(meus_itens_invertido)

# exibindo a lista ordenada e de uma maneira mais "humana"
print()
print("Exibição da lista em ordem alfabética")
for x in range(len(meus_itens)):
    print(f"item {x+1}: {meus_itens[x]} ")

''''''



