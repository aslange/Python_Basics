# -*- coding: utf-8 -*-

w = open('file.txt', 'w+', encoding='utf-8')
w.write('Esse é o meu arquivo!')
w.close()

arquivo = open('file.txt', 'r', encoding='utf-8')

print(arquivo)
print(arquivo.read())