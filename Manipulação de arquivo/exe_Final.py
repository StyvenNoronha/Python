from agenda import add,delete,list_contacts

while True:
    print("--- Opções Agenda de Contatos ---")
    print("1. Adicionar Contato")
    print("2. Lista Contato")
    print("3. remover todos Contatos") 
    print("4. Sair") 

    escolha = input("Escolha um opção\n")

    if escolha == "1":
        add()
    elif escolha == "2":
        list_contacts()
    elif escolha == "3":
        delete()
    elif escolha == "4":
        break
    else:
        print("Não tem essa opção")    
