num = int(input("Enter a number: "))
num1 = int(input("Enter a number: "))
operacao = input("Enter a operator: (+,-,*,/): ")
if operacao == "+":
    print(num + num1)
elif operacao == "-":
    print(num - num1)
elif operacao == "*":
    print(num * num1)
elif operacao == "/":
    print(num / num1)
else:
    print("Invalid operator")