estoque_disponivel = True 
cliente_premium = True 
frete_gratis = True 
if not (not estoque_disponivel or (not (not cliente_premium or frete_gratis))): 
    print("Pedido validado: Prosseguir para pagamento.") 

else: print("Pedido retido: Verifique as condições de frete e estoque.")