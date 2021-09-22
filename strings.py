a = "Augusto"
b = "Lange"

concatenar = a + b
concatenar2 = a + " " + b
concatenar3 = a + " " + b + "\n"

print(concatenar)
print(concatenar2)

print(len(concatenar))

letra = concatenar2[8]

print(letra)
print(concatenar2[0:9] + ".")

minusculo = (concatenar2[0:9] + ".").lower()
maiusculo = (concatenar2[0:9] + ".").upper()

print(minusculo)
print(maiusculo)

minha_string = "Oi, eu sou uma string"

minha_lista = minha_string.split(" ")
print(minha_lista)

busca = minha_string.find("sou")
print(busca)

busca2 = minha_string.find("ajax")
print(busca2)

minha_string = minha_string.replace("string", "lista")
print(minha_string)