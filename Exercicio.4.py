## 

qtd_pares = 0
qtd_impares = 0
soma_pares = 0
soma_impares = 0

for i in range(1, 11):
    numero = int(input(f"Digite o {i}º número: "))

    if numero % 2 == 0:
        qtd_pares += 1        
        soma_pares += numero   
    else:
        qtd_impares += 1      
        soma_impares += numero 

print("\nResultados")
print("Quantidade de números pares:", qtd_pares)
print("Quantidade de números ímpares:", qtd_impares)
print("Soma dos números pares:", soma_pares)
print("Soma dos números ímpares:", soma_impares)