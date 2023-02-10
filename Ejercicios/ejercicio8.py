from random import randint

lista_aleatoria = [randint(1,100) for i in range (0,10)]
lista_inv= lista_aleatoria [::-1]
print(f"lista sin cambios {lista_aleatoria}")
print(f"lista invertida {lista_inv}")