# função zip()

lista1 = [1, 2, 3, 4, 5]
lista2 = ["abacate", "bola", "cachorro", "dado", "elefante"]
lista3 = ["R$ 2,00", "R$ 3,00", "R$ 500,00","R$ 56,00", "R$ 19.400,00"]

for numero, nome, valor in zip(lista1, lista2, lista3):
    print(numero, nome, valor)