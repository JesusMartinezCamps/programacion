#Introducir dos numeros por teclado y luego intercambiar sus valores, por ultimo mostrar el resultado

print("Introduce el primer numero:")
numero1 = input()

print("Introduce el segundo numero:")
numero2 = input()

numero3 = numero1
numero1 = numero2
numero2 = numero3

print("El primer numero vale ahora", numero1, "y el segundo numero vale ahora", numero2)