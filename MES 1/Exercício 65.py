texto = str(input("Digite uma frase: "))
VOGAL = "A"

for letra in texto:
    if letra.upper() in VOGAL:
        print(letra, end="")
print()
print("Quantidade: ", texto.upper().count("A"))



