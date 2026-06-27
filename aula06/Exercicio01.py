possui_token = True 
ip_conhecido = False 
sistema_atualizado = True 
tentativas_excedidas = False

if possui_token and ip_conhecido:
    print("Acesso Nível 1 Liberado")


if sistema_atualizado and not tentativas_excedidas: 
    print("Acesso Nível 3: Verificação de Integridade")