contatos = []
rodando = True
while rodando:
    print("\nMenu da Agenda de Contatos: ")
    print("1. Adicionar um contato")
    print("2. Visualizar a lista de contatos")
    print("3. Editar um contato")
    print("4. Marcar ou desmarcar um contato como favorito")
    print("5. Ver a lista de contatos favoritos")
    print("6. Apagar um contato")
    print("7. Sair")
    
    escolha = input("Digite a sua escolha: ")

    if escolha == "1":
        rodando = True

    elif escolha == "7":
        rodando = False
        print("\nPrograma Finalizado!")