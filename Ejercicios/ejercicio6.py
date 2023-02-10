list_num = []
num_usua= int(input("Por favor, ingresa un número: "))
list_num.append(num_usua)
mas_num = input("¿desea agregar más números?: ")
while mas_num == 's' or mas_num =='S':
    num_usua= int(input("Por favor, ingresa un número: "))
    list_num.append(num_usua)
    mas_num = input("¿desea agregar más números?")
print(f"los números ingresados por el usuario son: {list_num}")
suma = 0
for x in list_num:
    suma= suma + x
print(f"la suma de la lista es: {suma}")
input("por favor, presione cualquier letra para salir.")


