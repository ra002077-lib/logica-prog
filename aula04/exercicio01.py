#### EXERCÍCIO 1: Em uma cozinha de restaurante existem apenas os ingredientes a seguir. 
#Exiba todas as possíveis combinações (não importa a sequência)
#utilizando até 3 ingredientes e quantas receitas isto totaliza.
#Ingredientes disponíveis: tomate, agrião, filé de frango, pão de queijo, mel.
#obs.: não se esqueça de eliminar combinações de nomes iguais.

''''''

""""""

ingredientes = ('tomate', 'agrião', 'filé de frango', 'pão de queijo', 'mel')
contador = 0
for a in ingredientes:
    for b in ingredientes:
        for c in ingredientes:
            if (a != b) and (b != c) and (a != c):

                print(f'{a} com {b} e {c}')
                contador+=1
print(f'Foram um total de {contador} combinações.  ')
