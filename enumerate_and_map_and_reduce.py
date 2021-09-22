# função enumerate

lista = ['abacate', 'bola', 'cachorro'] # lista

for i in range(len(lista)):
    print(i, lista[i])

for i, nome in enumerate(lista):
    print(i, nome)

# função map

def dobro(x):
    return x * 2

valor = [1, 2, 3, 4, 5]

print(dobro(valor))

valor_dobrado = map(dobro, valor)
valor_dobrado = list(valor_dobrado)

print(valor_dobrado)

# função reduce

from functools import reduce

def soma(x, y):
    return x + y

lista = [1, 2, 3, 4, 5]

soma = reduce(soma, lista)
print(soma)