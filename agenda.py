def adicionar_contato(contatos, nome_contato, numero_contato, email_contato):
    contato = {"contato": nome_contato, "telefone": numero_contato, "email": email_contato, "favorito": False}
    contatos.append(contato)
    print(f"\nContato de {nome_contato} adicionado com sucesso!")
    return

def ver_contatos(contatos):
    print("\nLista de contatos:")
    for indice, contato in enumerate(contatos, start=1):
        status = "✩" if contato["favorito"] else " "
        nome_contato = contato["contato"]
        print(f"{indice}. [{status}] {nome_contato} | {numero_contato} | {email_contato}")
    return

def editar_contato(contatos):
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
        indice_contato = int(input("Digite o número do contato que deseja atualizar: "))
        

    elif escolha == "7":
        rodando = False
        print("\nPrograma Finalizado!")