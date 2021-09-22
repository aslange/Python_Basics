try:
    intNumber1 = int(input("Digite seu primeiro numero: "))
    intNumber2 = int(input("Digite seu segundo numero: "))
    intNumber3 = int(input("Digite seu terceiro numero: "))
except:
    print("Você não digitou numeros!")
    quit()

lstListaNumerica = [intNumber1, intNumber2, intNumber3]

print(lstListaNumerica)

lstListaNumerica.sort()

print(lstListaNumerica)