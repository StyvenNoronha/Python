import webbrowser

done = False

while not done:
    print(" Oque voce deseja fazer?")
    print("1.aprender python")
    print("2.aprender python e módulos")
    print("3.aprender python e fullstack")
    print("4.Sair")

    choice = input(">")

    if choice == "1":
        webbrowser.open("https://www.python.org/")
    elif choice == "2":
        webbrowser.open("https://docs.python.org/pt-br/3/tutorial/modules.html")  
    elif choice == "3":
        webbrowser.open("https://www.youtube.com/")    
    elif choice == "4":
        done =True   
    else:
        print("opção invalida")       