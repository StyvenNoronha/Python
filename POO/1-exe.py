class Movie:
    def __init__(self,name,yearLaunch, includePlan,durationMinutes):
        self.name = name
        self.yearLaunch = yearLaunch
        self.includePlan = includePlan
        self.totalEvaluation = 0
        self.durationMinutes = durationMinutes
        self.evaluators = 0

    def __str__(self):
        return f"Filme :{self.name}"
    
    def technical_sheet(self):
        print("dados do filme")
        print(f"Nome do filme: {self.name}")
        print(f"Ano de lançamento: {self.includePlan}")
        print(f"Avaliação do filme: {self.totalEvaluation}")
        print(f"duração do filme: {self.durationMinutes}")
        print(f"Total de avaliadores {self.evaluators}")

    def evaluate(self, note):
        self.totalEvaluation += note
        self.evaluators += 1

    def avagare(self):
        print(f"Media do filme é {self.name}: { self.totalEvaluation / self.evaluators} ")

naruto = Movie("naruto last movie",2017,True,120)
avatar = Movie("Avatar a lenda de Ang",2017,False,210)


naruto.evaluate(9.5)
naruto.evaluate(8.0)
naruto.technical_sheet()
naruto.avagare()


avatar.evaluate(10)
avatar.evaluate(9)
avatar.evaluate(8)
avatar.evaluate(7)
avatar.avagare()
avatar.technical_sheet()
