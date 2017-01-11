#Pedir dos numeros, y decir si es el primero es mayor, el primero es menor o son iguales

print("Introduce un primer numero:")
valor1 = input()

print("Introduce un segundo numero:")
valor2 = input()

if valor1 > valor2:
	print("El primer numero", valor1, "es mayor que el segundo numero", valor2)
elif valor1 < valor2:
	print("El primer numero", valor1, "es menor que el segundo numero", valor2)
else:
	print("El primer numero", valor1, "es igual que el segundo numero", valor2)