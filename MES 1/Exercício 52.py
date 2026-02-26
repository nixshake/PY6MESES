senha = int(input("Digite a sua senha (3 dígitos): "))

while senha != 123:
    print("Senha incorreta")
    senha = int(input("Digite novamente: "))
print("Senha correta!")