#Pedir dos numeros enteros y mostrar su suma SOLO SI SON POSITIVOS. "La suma de los dos numeros es: XXX"
#Mensaje que especifique que numero/s es negativo.
print("Introduce tu primer numero:")
valor1 = input()

print("Introduce tu segundo numero:")
valor2 = input()

resultado = valor1 + valor2

if valor1 >= 0 & valor2 >= 0:
	print("La suma de los dos numeros es: ", resultado)
elif valor1 < 0 & valor2 >= 0:
	print("No se calcula la suma porque el primer numero", valor1, "es negativo")
elif valor2 < 0 & valor1 >= 0:
	print("No se calcula la suma porque el segundo numero", valor2, "es negativo")
else valor1 < 0 & valor2 < 0:
	print("No se calcula la suma porque ambos numeros son negativo")