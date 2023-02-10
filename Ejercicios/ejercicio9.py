filas= int(input("Ingrese el número de filas que quiera: "))
columnas= int(input("Ingrese el número de columnas que quiera: "))
matriz= []
for i in range(filas):
    matriz.append([])
for j in range(columnas):
    valor = float(input("Fila {}, colmna {} ".format(i+j, j+i)))
    matriz[i].append(valor)

print()
for fila in matriz:
    print("[", end= "")
    for elemento in fila:
        print("{8.2f}".format(elemento), end= "")
        print("]")
print()
