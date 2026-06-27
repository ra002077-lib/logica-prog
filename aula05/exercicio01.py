possibilidade = [True, False]
print("________________________")
print("Formula: (M v N ) ^ ¬(Q v P) ^ (¬M v Q) ^ (¬N v R) ")
print("________________________")
linhas = 0
for M in possibilidade:
    for N in possibilidade:
        for O in possibilidade:
            for P in possibilidade:
                for Q in possibilidade:
                    for R in possibilidade:
                        if (M or N) and not (O or P) and (not M or Q) and (not N or R):
                            res_f = 'Verdadeiro'
                            contado = 0
                        else:
                            res_f = 'Falso'
                            contador = 0
                        print(f"M = {M} \tN = {N} \tO = {O} \tP = {P} \tQ = {Q} \tR = {R} \tFórmula = {res_f}")
                        linhas += 1
print(f"Total de linhas : {linhas} ")