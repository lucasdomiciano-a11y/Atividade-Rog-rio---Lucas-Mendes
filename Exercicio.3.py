## Soma de 10 números

soma = 0

for i in range(10):
    numero = float(input(f"Digite o {i + 1}º número: "))
    soma += numero

print(f"A soma dos números é: {soma}")