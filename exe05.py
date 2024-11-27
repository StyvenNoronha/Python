#verifica se letra e Uppercase e lowercase
def checkChar(text):
    type = {"UpperCase": 0, "LowerCase":0}
    for char in text:
        if char.isupper():
            type["UpperCase"] += 1
        elif char.islower():
            type["LowerCase"] += 1
    print("Texto original", text)
    print(type["UpperCase"])              
    print(type["LowerCase"])              

checkChar("A Batata E Legal")

def checkEvenOdd(list):
    par = []
    impar = []
    for n in list:
        if n % 2 == 0:
            par.append(n)
        else:
            impar.append(n)

    print(par)
    print(impar)
      

checkEvenOdd([1,2,3,4,5,6,7,8,9,10])