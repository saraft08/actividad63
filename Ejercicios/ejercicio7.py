import heapq

list_num = []
num_usua= int(input("Por favor, ingresa un número: "))
list_num.append(num_usua)
mas_num = input("¿desea agregar más números?: ")
while mas_num == 's' or mas_num =='S':
    num_usua= int(input("Por favor, ingresa un número: "))
    list_num.append(num_usua)
    mas_num = input("¿desea agregar más números?")
print(f"los números ingresados por el usuario son: {list_num}")
print(f"el número mayor es: {heapq.nlargest(1,list_num)}")
print(f"el número menor es: {heapq.nsmallest(1,list_num)}")

