import os

def add():
    name = input("informe o nome\n")
    address = input("Informe o endereço\n")
    phone = input("Informe seu numero")

    contact = f"Name: {name} \nAddress:{address} \n Phone: {phone} \n"

    with open("agenda.txt","a",encoding="utf-8") as file:
        file.write(contact)

def list_contacts():
    if not os.path.exists("agenda.txt"):
        print("não existe a agenda")
        return
    with open("agenda.txt",'r', encoding="utf-8") as file:
        print("Sua lista de contatos")
        for line in file:
            print(f"{line.rstrip()}")

def delete():
        if not os.path.exists("agenda.txt"):
            print("não existe a agenda")
            return
        with open("agenda.txt",'w', encoding="utf-8") as file:
            file.write("")

delete()    