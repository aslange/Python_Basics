# list comprehension

x = [1, 2, 3, 4, 5]
y = []

for i in x:
    y.append(i ** 2)

print(x)
print(y)

y2 = [i ** 2 for i in x]

print("usando o list comprehension")
print(x)
print(y2)

z = [i for i in x if i % 2 == 1]

print(z)
