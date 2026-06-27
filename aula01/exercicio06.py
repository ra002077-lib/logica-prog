#Cardápio de MArmitas Fitness,
#Crie  tres listas : proteinas, carboidratos e saladas. 
# Sistema deve gerar as opções de montagem de marmitas para a semana, seguindo estas diretrizes:

print("OPÇÕES DE MARMITAS: ")
proteinas = ['Peixe', 'Ovo', 'Frango']
carboidratos = ['Batata doce','Arroz', 'Quinoa']
saladas = ['Espinafre','Alface', 'Brócolis']

#Regra 1 Não é permitido combinar Peixe com Batata doce.
#Regra 2 A escolha de salada Espinafre deve ocorrer se e somente se a primeira for Ovo. (Biimplicação)
#Regra 3 Não se esqueça de eliminar combinações de nomes iguais caso algum ingrediente se repita nas listas.


for p in proteinas:
    for c in carboidratos:
        for s in saladas:
            if (not (p == 'Peixe' and c == 'Batata doce')) and ((s == 'Espinafre') == (p == 'Ovo')) and (p != c and c != s and p != s):
                print(f"Marmitas: {p} + {c} + {s}")
             