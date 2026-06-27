possibilidade = [True, False]

total_de_linhas = 0
total_F = 0
total_T = 0
quant_variaveis = input(f"Digite quantidade de variáveis desejadas (entre 2 ou 3): ")
qual_formula = input(f"Digite a fórmula (use P, Q e R como variáveis:):").lower()


for p in possibilidade:
    for q in possibilidade:
        for r in possibilidade:
            if eval(qual_formula):
                res_f = 'Verdadeiro'
                total_T += 1
                
            else:
                res_f = 'Falso'
                total_F += 1
                           

            print(f"P = {p} \tQ = {q} \tR = {r} \tFórmula = {res_f}")

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
print(f"Esta fórmula é \033[1m{propriedade_semantica}\033[0m")