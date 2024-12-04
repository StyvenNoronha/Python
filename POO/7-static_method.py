"""
1 - O método estático não possui o parâmetro self.
2 - O método de classe pode acessar mas não pode modificar o estado da classe 
3 - Usamos o decorator @staticmethod em python para criar um método estático
""" 

class Course:
    def __init__(self, name, trail):
        self.name = name
        self.trail = trail


    @staticmethod
    def courses_trail(trail):
        if trail == 'Python Fundamentos':
            courses = ['Dominando o Python', 'Módulos e Pip', 'Orientação a Objetos']
        elif trail == 'Automação com Python':
            courses = ['Automação de Tarefas', 'Web Scraping', 'Assistente Virtual']
        else:
            courses = ['A definir']
        return courses

print(Course.courses_trail('Python Fundamentos'))
print(Course.courses_trail('Automação com Python'))
print(Course.courses_trail('IA'))        