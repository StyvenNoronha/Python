def sum(*num):
    sumTotal = 0
    for n in num:
        sumTotal += n
    print(sumTotal)        

sum(5,8,9,4)    



#apresentação de curso
def presentation(**data):
    for key, value in data.items():
        print(f"{key} - { value}")


presentation(
    curso="Python",
    categoria="backend",
    level="iniciante"
)        