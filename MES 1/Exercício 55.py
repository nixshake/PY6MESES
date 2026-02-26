soma = 0
numero = int(input("Digite um número: (-1 pra parar): "))

while numero != -1:
    soma += numero
    numero = int(input("Digite um número: (-1 pra parar): "))

print(f"A soma total é: {soma}")
