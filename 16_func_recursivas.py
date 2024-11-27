#factorial de um numero
def fac(num):
    if num == 1:
        return num
    else:
        return (num * fac(num -1))


#print(fac(5))


def soma(num):
    if num == 1:
        return num
    else:
        return (num + soma(num -1))
    

print(soma(6)  )  