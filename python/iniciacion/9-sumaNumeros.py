#Pedir dos numeros enteros y mostrar su suma SOLO SI SON POSITIVOS. "La suma de los dos numeros es: XXX"
#Si no son positivos sale un mensaje que lo muestra "No se calcula la suma porque alguno de los dos numeros o los dos no son positivos"
print("Introduce tu primer numero:")
valor1 = input()

print("Introduce tu segundo numero:")
valor2 = input()

resultado = valor1 + valor2

if valor1 >= 0 & valor2 >= 0:
	print("La suma de los dos numeros es: ", resultado)
else:
	print("No se calcula la suma porque alguno de los dos numeros o los dos no son positivos")