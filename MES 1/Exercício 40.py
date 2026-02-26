user_cadastrado = "sofia"
senha_cadastrada = "12345678"

user = input("Usuário: ")
senha = input("Senha: ")

if user == user_cadastrado and senha == senha_cadastrada:
    print("Login realizado")
else:
    print("Usuário ou senha incorretos")