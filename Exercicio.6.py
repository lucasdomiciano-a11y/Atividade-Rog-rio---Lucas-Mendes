## para informar idade e nome de pessoas. São 5 pessoas. Ao final deverá mostrar o nome e a idade da pessoa mais velha.

nome_mais_velho = ""
maior_idade = 0

for i in range(5):
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))

    if idade > maior_idade:
        maior_idade = idade
        nome_mais_velho = nome

print(f"\nA pessoa mais velha é {nome_mais_velho} com {maior_idade} anos.")