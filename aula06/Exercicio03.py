valor_compra= int(input("Digite o valor da compra: R$  "))
possui_cupom= bool(input("Possui cupom: (s/n)"))
cliente_fidelidade= bool(input("É cliente fidelidade: (s/n)"))
desconto_fidelidade = valor_compra - (valor_compra * 0.20)
desconto= valor_compra - (valor_compra * 0.05)

if (valor_compra > 100 ) == cliente_fidelidade:
    print(f"O valor da compra é {desconto_fidelidade}")

else:
    print(f"O valor da compra é {desconto} Reais")

