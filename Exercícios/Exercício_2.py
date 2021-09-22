try:
    floatScore1 = float(input("Digite sua primeira nota: "))
    floatScore2 = float(input("Digite sua segunda nota: "))
except:
    print("Você não digitou notas válidas!")
    quit()

floatMedian = (floatScore1 + floatScore2) / 2

if floatMedian >= 6:
    print("Você está aprovado!")
else:  
    print("Você está reprovado. Continue estudando e tentando.")