nota = int(input("Qual foi a sua nota? "))

if nota >= 0 and nota <= 10:
    print(f"Sua nota foi {nota}")
else:
    print("Nota inválida")