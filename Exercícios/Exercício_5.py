try:
    intNumber1 = int(input("Digite seu primeiro numero: "))
    strOperator = input("Digite a operação (+, -, *, /): ")
    intNumber2 = int(input("Digite seu segundo numero: "))
except:
    print("Você não digitou numeros!")
    quit()

if strOperator == "+":
    intResult = intNumber1 + intNumber2
elif strOperator == "-":
    intResult = intNumber1 - intNumber2
elif strOperator == "*":
    intResult = intNumber1 * intNumber2
elif strOperator == "/":
    intResult = intNumber1 / intNumber2
else:
    print("Você não digitou uma operação válida!")
    quit()

print(intResult)