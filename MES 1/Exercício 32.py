idade = int(input("Qual a sua idade? "))
cnh = str(input("Possui CNH(sim/não)? "))

if idade >= 18 and cnh == "sim":
    print("Pode dirigir")
else:
    print("Não pode dirigir")