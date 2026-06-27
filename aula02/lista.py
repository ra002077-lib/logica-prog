print("Criando uma lista e fazendo sua exibição")
Comidas = ["Pizza", "Churrasco", "Sorvete", "Bacon", "Hotdog", "Alface"]
print(Comidas)

len(Comidas) # conta o tamanho da lista
print(len(Comidas)) #imprime resultado do comando

tamanho_da_lista = len(Comidas) # jogou o tamanho para variavel
print(tamanho_da_lista) # imprimindo a variavel com tamanho da lista

texto = "obabaotudobao"
print(f"O tamanho de text é {len(texto)}")


print(Comidas[0]) # imprime o primeiro elemento da lista
print(Comidas[2]) # imprime o 3° elemento

print(f'O ultimo elemento é "{Comidas[-1]}"')

# gerando uma lista
range(10) # cria um objeto referente a esta faixa de dados
list(range(10)) # gera a lista com base na faixa definida
print(list(range(10))) # imprime o range como lista
print(list(range(10,30)))
print(list(range(20,30,2)))

print(f"Comidas = {Comidas}")
Comidas.reverse()
print(f"Comidas = {Comidas}")

Comidas.append("lasanha") # Adiciona item ao final da lista
print(f"Comidas = {Comidas}")

Comidas.insert(0,"Feijoada") # Adiciona na primeira posição da lista
print(f"Comidas = {Comidas}")
