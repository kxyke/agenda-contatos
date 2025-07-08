def adicionar_contato(contatos, nome_contato, numero_contato, email_contato):
    contato = {"contato": nome_contato, "telefone": numero_contato, "email": email_contato, "favorito": False}
    contatos.append(contato)
    print(f"\nContato de {nome_contato} adicionado com sucesso!")
    return

def ver_contatos(contatos):
    print("\nLista de contatos:")
    for indice, contato in enumerate(contatos, start=1):
        status = " ✩ " if contato["favorito"] else " "
        nome_contato = contato["contato"]
        numero_contato = contato["telefone"]
        email_contato = contato["email"]
        print(f"{indice}. [{status}] {nome_contato} | {numero_contato} | {email_contato}")
    return

def atualizar_nome_contato(contatos, indice_contato, novo_nome_contato):
    indice_contato_ajustado = indice_contato -1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        contatos[indice_contato_ajustado]["contato"] = novo_nome_contato
        print(f"Nome do Contato {indice_contato}. atualizado para {novo_nome_contato}")
    else:
        print("Índice de tarefa inválido.")
    return

def atualizar_numero_contato(contatos, indice_contato, novo_numero_contato):
    indice_contato_ajustado = indice_contato -1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        contatos[indice_contato_ajustado]["telefone"] = novo_numero_contato
        print(f"Número do Contato {indice_contato}. atualizado para {novo_numero_contato}")
    else:
        print("Índice de tarefa inválido.")
    return

def atualizar_email_contato(contatos, indice_contato, novo_email_contato):
    indice_contato_ajustado = indice_contato -1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        contatos[indice_contato_ajustado]["email"] = novo_email_contato
        print(f"Email do Contato {indice_contato}. atualizado para {novo_email_contato}")
    else:
        print("Índice de tarefa inválido.")
    return

def menu_editar_contato(contatos):
    indice_contato = int(input("\nDigite o indice do contato que deseja editar: "))
    if indice_contato < 1 or indice_contato > len(contatos):
        print("Índice inválido. Tente novamente.")
        menu_editar_contato(contatos)
        return

    opcao = 0
    while opcao != 4:
        print("\nO que você deseja editar?")
        print("[1] Nome; \n[2] Número; \n[3] Email; \n[4] Sair.")
        try:
            opcao = int(input("Digite sua opção: "))
        except ValueError:
            print("Digite um número válido.")
            continue

        if opcao == 1:
            novo_nome_contato = input("Digite o novo nome do contato: ")
            atualizar_nome_contato(contatos, indice_contato, novo_nome_contato)
                
        elif opcao == 2:
            novo_numero_contato = input("Digite o novo número do contato: ")
            atualizar_numero_contato(contatos, indice_contato, novo_numero_contato)

        elif opcao == 3:
            novo_email_contato = input("Digite o novo email do contato: ")
            atualizar_email_contato(contatos, indice_contato, novo_email_contato)
        
        elif opcao == 4:   
            print("Saindo do menu de edição...")

        else:
            print("Opção inválida, tente novamente.")

def adicionar_favorito(contatos, indice_contato):
    indice_contato_ajustado = indice_contato -1
    contatos[indice_contato_ajustado]["favorito"] = True
    print(f"Contato {indice_contato} adicionado aos favoritos!")
    return

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
        nome_contato = input("Digite o nome do contato que deseja adicionar: ")
        numero_contato = input(f"Digite o número do {nome_contato}: ")
        email_contato = input(f"Digite o email do {nome_contato}: ")
        adicionar_contato(contatos, nome_contato, numero_contato, email_contato)

    elif escolha == "2":
        ver_contatos(contatos)
    
    elif escolha == "3":
        ver_contatos(contatos)
        menu_editar_contato(contatos)

    elif escolha == "4":
        ver_contatos(contatos)
        indice_contato = int(input("\nDigite o indice do contato que deseja editar: "))
        adicionar_favorito(contatos, indice_contato)

    elif escolha == "7":
        rodando = False
        print("\nPrograma Finalizado!")