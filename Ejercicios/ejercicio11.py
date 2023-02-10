from random import randint

lista_aleatoria = [randint(1,100) for i in range (0,10)]
print(lista_aleatoria)
for x in lista_aleatoria:
    if x % 2 == 0:
        print(x)
