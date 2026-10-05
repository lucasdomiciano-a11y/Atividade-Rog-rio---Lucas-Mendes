## F.U.P que calcule a média dos números digitados pelo usuário, se eles forempares. Sendo que são 5 números.

qtd_pares = 0
soma_pares = 0
for i in range(5):
    numero = int(input(f"Digite o {i + 1}º número: "))

    if numero % 2 == 0:
        qtd_pares += 1        
        soma_pares += numero

if qtd_pares > 0:   
    media_pares = soma_pares / qtd_pares
    print("A média dos números pares é:", media_pares)
    
