teams = {}
done = False

#função para listar times


#Opção 3 = lista de times 
def print_teams():
    for i, team in enumerate(teams.values()):
        print(f"{i+1}. {team['name']} ({len(team['players'])} jogadores)")

#opção 6  = lista de jogadores
def print_team_players(team):
    print(f"Jogadores do {team['name']}")
    for i, player in enumerate(team['players']):
        print(f"{i+i}. {player}")        
while not done:
    #opção no programa
    print("O que deseja fazer")
    print("1. add time")
    print("2.remover time")
    print("3.Listar times")
    print("4.add jogador e um time")
    print("5.remover jogador e um time")
    print("6.Listar jogadores de um time")
    print('7. Sair')

    choice = input(">") 
    if choice == "1":
        team_name = input("Digite o nome do time \n")
        teams[team_name] = {'name': team_name, 'players':[]}
        print("Time adicionado com sucesso")
    elif choice == "2":
        print_teams()
        teamNum = int(input("Informe o numero do time que deseja remover\n"))
        if teamNum <= len(teams):
            team_name = list(teams.keys())[teamNum -1]
            del teams[team_name]
            print('time removido com sucesso')
        else:
            print('erro')    
    elif choice == "3":
        print_teams()
        
    elif choice == "4":
        print_teams()
        team_num = int(input("informe o numero do time que deseja adicionar o jogador"))
        if team_num <= len(teams):
            team_name = list(teams.keys())[team_num -1]
            player_name = input("informe o nome do jogador\n")
            teams[team_name]['players'].append(player_name)
            print("jogador adiciona com sucesso")
        else:
            print("Numero do time inválido")    
    elif choice == "5":
        print_teams()
        team_num = int(input("informe o numero do time que deseja remover o jogador"))
        if team_num <= len(teams):
            team_name = list(teams.keys())[team_num -1]
            print_team_players(teams[team_name])  

                                           

    elif choice == "6":
        print_teams()
        team_num = int(input("informe o numero do time que deseja listar o jogador"))
        if team_num <= len(teams):
            team_name = list(teams.keys())[team_num -1]  
            print_team_players(teams[team_name])   
            player_num = int(input("informe o numero do jogador que deseja remover\n")) 
            if player_num <= len(teams[team_name]['players']):
                del teams[team_name]['players'][player_num -1]     
                print('jogador removido com sucesso')
            else:
                print('numero do jogador invalido')
        else:
            print('numero do time invalido')           

    elif choice == "7":
        done = True
    else:
        print("Não tem essa opção")
    
        

                            
