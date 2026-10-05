## Calculo para idade de Votação

nome = input("Escreva seu nome: ")
ano_atual = int(input("Digite o ano em que estamos: "))
ano_nascimento = int(input("Digite seu ano de nascimento: "))

idade = ano_atual - ano_nascimento

if idade >= 18:
    print("Você pode fazer a carteira de motorista")

elif idade >= 16:
    print("Você pode votar")

else:
    print("Você é menor de idade")