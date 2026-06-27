camisas = ['Social', 'Verde', 'Regata']
calcas = ['Jeans', 'Azul', 'Bermuda']
calcados = {'Tênis', "Sapato"}

for a in camisas:
    
    for b in calcas:
        
        for c in calcados:
       
            if (not (a == 'verde' and b == 'azul')) and (c == 'Tênis' or c != 'Social'):
                    print(f"Sugestão: {a}, {b} e {c}")
        
