# Recursividade
comidas = ['bacon', 'lasanha', 'churrasco']
frutas = ['pera', 'uva', 'jabuticaba']

for x in comidas:
    print(x)

for y in frutas:
    print(y)
contador = 0
for x in comidas:
    for y in frutas:
        print(x,y)
        contador+=1
print(f'Foram identificados {contador} combinações.')



