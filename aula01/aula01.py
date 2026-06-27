a = "hello"
b = "world"
print(a,b)
print(a+b)
print(10+4)
print(1.5+2.5)
st = "sistemas de informação"
print(st)
print(st[3:10])
print(st[:5])
print(st[:3],st[19:])

print(st[::-1])
print(st[::-1].upper())
print(st[::-1].isupper())
st2 = st[::-1].upper()
print(st2)
st3 = st.upper()
print(st3)

VALOR = 33
print(f"O valor da variavel Valor é, {VALOR}")

print("Vamos definir as cores do time:")
cor1 = input("Digite a primeira cor:")
cor2 = input("Digite a segunda cor:")
cor3 = input("Digite a terceira cor:")
if (cor1 == cor2 and  cor3 == cor1) or (cor1 != cor2 and cor1 != cor3):
    definição = "ÓTIMA ESCOLHA DE CORES"
else:
    definição = "PÉSSIMA ESCOLHA DE CORES"