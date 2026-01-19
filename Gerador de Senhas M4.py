import random

print("=== CRIAR CONTA NO APLICATIVO ===")

nome = input("Digite seu nome: ")


email = input("Digite seu e-mail: ")
while "@" not in email:
    print("E-mail inválido. O e-mail precisa conter @")
    email = input("Digite seu e-mail novamente: ")

usuario = input("Digite um nome de usuário: ")


palavra = input("Digite uma palavra para gerar sua senha: ")

numeros = "0123456789"

senha = palavra.lower()

senha = senha[0].upper() + senha[1:]


for i in range(3):
    senha += random.choice(numeros)

print("\n=== CONTA CRIADA COM SUCESSO ===")
print("Nome:", nome)
print("E-mail:", email)
print("Usuário:", usuario)
print("Senha gerada:", senha)
print("Tamanho da senha:", len(senha))
