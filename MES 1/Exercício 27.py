nota = int(input("Digite a sua nota: "))

if nota < 5:
    print("Reprovado")
elif nota >= 5 and nota <= 6.9:
    print("Recuperação")
elif nota >= 7:
    print("Aprovado")
