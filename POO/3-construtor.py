class Movie:
    def __init__(self,name,yearLaunch, includePlan,note,durationMinutes):
        self.name = name
        self.yearLaunch = yearLaunch
        self.includePlan = includePlan
        self.note = note
        self.durationMinutes = durationMinutes

    def __str__(self):
        return f"Filme :{self.name}"

movie = Movie("naruto",2023,True,8.6,130)
'''
print(movie.name)    
print(movie.yearLaunch)    
print(movie.includePlan)    
print(movie.note)    
print(movie.durationMinutes)
'''
print(movie)

