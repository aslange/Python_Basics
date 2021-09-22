# -*- coding: utf-8 -*-

minha_lista = ["abacaxi", "banana", "cereja", "damasco", "figo", "goiaba", "jabuticaba", "kiwi", "laranja", "manga", "nectarina", "pêra", "quiabo", "rambutan", "siri", "tangerina", "uva", "watermelon", "xeremóia", "yagua", "zabumba"]
minha_lista2 = [1,2,3,4,5]
minha_lista3 = ["abacaxi", 2, 8.99, True]

tamanho = len(minha_lista)
print(tamanho)

minha_lista.append("limão")
print(minha_lista)

del minha_lista[2:]
print(minha_lista)

del minha_lista

lista = [124, 345,3,495,382, 4,2, 6,7,8,1]

print(lista)

lista.sort()

print(lista)

lista.sort(reverse = True)

print(lista)

#######################
# Dicionários
#######################

# dicionarios em python
dicionario_sites = {"Google": "google.com", "Udemy": "udemy.com"}

print(dicionario_sites)
print(dicionario_sites['Google'])
 
for chave in dicionario_sites:
    print(chave + " - " + dicionario_sites[chave])

print(dicionario_sites.keys())
print(dicionario_sites.values())