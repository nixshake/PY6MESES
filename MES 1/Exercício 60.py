while True:
    print("\n --- MENU ---")
    print("[1] - Dizer Olá")
    print("[2] - Mostrar número 10")
    print("[3] - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("Olá!")
    elif opcao == "2":
        print("10")
    elif opcao == "3":
        print("Encerrando programa...")
        break
    else:
        print("Opção inválida.")