tintas = ['Óleo', 'Látex', 'Acrílica']
pinceis = ['Rolo','Cerda', 'Esponja']
solventes = ['Água', 'Aguarás', 'Thinner']
contador = 0
for t in tintas:
    for p in pinceis:
        for s in solventes:
            if (not (t == 'Óleo' and s == 'Água')) and (p == 'Rolo' or t != 'Látex'):
                print(f"Projeto: {t}, {p} e {s}")
                contador+=1
print(f"Foram definidas {contador} combinações: ")