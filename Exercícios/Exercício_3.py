""" intNumber1 = input("Digite x para resolver f(x) = x^2: ")

isValuesNumeric = intNumber1.isnumeric()

if isValuesNumeric:
    intNumber1 = int(intNumber1)

    intResult = intNumber1**2

    print("f(" + str(intNumber1) + ") = " + str(intResult))
else:
    print("Você não digitou numeros!") """

from math import sqrt

try:
    intA = int(input("Digite o valor de A: "))
    intB = int(input("Digite o valor de B: "))
    intC = int(input("Digite o valor de C: "))
except:
    print("Você não digitou valores válidos")
    quit()

intDelta = ((intB ** 2) - (4 * intA * intC))

if intDelta < 0:
    print("Delta negativo")
else:
    floatSqrtDelta = sqrt(intDelta)

    floatRaizX1 = ((-intB + floatSqrtDelta) / (2 * intA))
    floatRaizX2 = ((-intB - floatSqrtDelta) / (2 * intA))
 
    print("As raízes são", floatRaizX1, "e", floatRaizX2)