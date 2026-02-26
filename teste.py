altura = float(input("Digite a altura: "))
peso = float(input("Digite o seu peso: "))
imc = peso / (altura ** 2)

if imc < 18.5:
    print("Abaixo do peso")
else:
    print("Peso normal")