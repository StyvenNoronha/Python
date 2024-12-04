class Movie:
    def __init__(self,name,yearLaunch, includePlan,note,durationMinutes):
        self.name = name
        self.yearLaunch = yearLaunch
        self.includePlan = includePlan
        self.note = note
        self.durationMinutes = durationMinutes

    def __str__(self):
        return f"Filme :{self.name}"
    
    def technical_sheet(self):
        print("dados do filme")
        print(f"Nome do filme: {self.name}")
        print(f"Ano de lançamento: {self.includePlan}")
        print(f"Avaliação do filme: {self.note}")
        print(f"duração do filme: {self.durationMinutes}")

naruto = Movie("naruto",2028,True,9.8,120)        
boruto = Movie("boruto",2030,False,9.7,258)


naruto.technical_sheet()
boruto.technical_sheet()