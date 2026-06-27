possibilidade = [True, False]
print("________________________")
print("Formula: (P v Q ) ^  ¬R")
print("________________________")
total_de_linhas = 0
total_F = 0
total_T = 0


for P in possibilidade:
    for Q in possibilidade:
        for R in possibilidade:
            if (P or Q) and not R:
                res_f = 'Verdadeiro'
                total_T += 1
                
            else:
                res_f = 'Falso'
                total_F += 1
                           

            print(f"P = {P} \tQ = {Q} \tR = {R} Fórmula = {res_f}")

            total_de_linhas += 1 

if(total_de_linhas == total_T):
    propriedade_semantica = 'TAUTOLOGICA'
elif(total_de_linhas == total_F):
    propriedade_semantica = 'CONTRADITORIA'
else:
    propriedade_semantica = 'SATISFATORIA'

print(f"Total de linhas da tabela: {total_de_linhas}")
print(f"Total de linhas com resultado True: {total_T}")
print(f"Total de linhas com resultado False: {total_F}")
print(f"Esta fórmula é {propriedade_semantica}")