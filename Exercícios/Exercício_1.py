try:
    intAge = int(input("Digite sua idade: "))
except:
    print("Você não digitou uma idade válida")
    quit()

if intAge >= 18:
    print("Você é maior de idade")
else:  
    print("Você é menor de idade")