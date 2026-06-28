print("="*60)
print("         COMPARADOR DE FÓRMULAS LÓGICA")
print("         INTRODUÇÃO À LÓGICA DE PROGRAMAÇÃO")
print("="*60)
possibilidade = [True, False]
linhas = 0
verdade = 0
falso = 0

# Entrada primeira fórmula
print("\nFórmula 1:")
tabelaum = []

formula = input("Digite a fórmula 1 (use a, b e c): ").lower()

for a in possibilidade:
    for b in possibilidade:
        for c in possibilidade:
            if eval(formula):
                res = "Verdadeiro"
                verdade += 1
                tabelaum.append(res)
            else:
                res = "Falso"
                falso += 1
                tabelaum.append(res)
            
            print(f"a = {a}\tb = {b}\tc = {c}\tResultado = {res}")
            linhas += 1


print(f"Total de linhas na tabela = {linhas}")
print(f"Total de linhas  VERDADE na tabela = {verdade}")
print(f"Total de linhas FALSO na tabela = {falso}")

if falso == 0:
    print("\033[1m(É Tautologia)\033[0m")
elif verdade == 0:
    print("\033[1m(É contraditório!)\033[0m")
else:
    print("\033[1m(É satisfatória)\033[0m")

# Entrada segunda fórmula
print("\nFórmula 2:")
tabeladois = []
verdade2 = 0
falso2 = 0
linhas2 = 0
formula2 = input("Digite a fórmula 2 (use a, b, e c): ").lower()

for a in possibilidade:
    for b in possibilidade:
        for c in possibilidade:
            if eval(formula2):
                res = "Verdadeiro"
                verdade2 += 1
                tabeladois.append(res)
            else:
                res = "Falso"
                falso2 += 1
                tabeladois.append(res)
            print(f"a = {a}\tb = {b}\tc = {c}\tResultado = {res}")

            linhas2 += 1


print(f"Total de linhas na tabela = {linhas2}")
print(f"Total de linhas  VERDADE na tabela = {verdade2}")
print(f"Total de linhas FALSO na tabela = {falso2}")

if falso2 == 0:
    print("\033[1m(É Tautologia)\033[0m")
elif verdade2 == 0:
    print("\033[1m(É contraditório!)\033[0m")
else:
    print("\033[1m(É satisfatória)\033[0m")


print("\n" + "=" * 60)
print("ANÁLISE DE EQUIVALÊNCIA")
print("=" * 60)

if formula == formula2:
    print("\u2705 As fórmulas são iguais! Tente novamente")
elif tabelaum == tabeladois:
    print("\u2705 As fórmulas são equivalentes!")
else:
    print("\u274C As fórmulas não são equivalentes!")

# ((a or b) and (not c)) == (b and c)
# ((a == (not b)) or c) == ((not c) and (not b))
# (a == (not c)) and ((not a) and b)
# ((not a) and b and c)
# algum outro par de sua escolha
# a and b and ( b and c)
# a or c or (b and c)

