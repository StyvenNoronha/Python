gamesSet = { "fifa", "pes", "nfs", "gta", "nfs", "zelda"}
newGames = {"zelda", "gta","nfs", "nfs","fifa", "pes",   }

#nao possibilita recuperar valores via fatiamento ou slide
#true e 1 são  considerados iguais
#buscar o tamanho do set
print(len(gamesSet))

#adicionar item de outro set
gamesSet.update(newGames)
print(gamesSet)

#remover item
gamesSet.remove("fifa")
print(gamesSet)
