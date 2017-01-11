def checkNumeroValido(numero):

    #assert isinstance(numero, int), "No es un numero"
    if  isinstance(numero, int) and numero >= 0:
        return True
    return False

## PROGRAMA PRINCIPAL ##

def factorial(numero):
    #numero = int(input("Introduce un numero entero: "))
    if checkNumeroValido(numero):
        if numero == 0 or numero == 1:
            print("El factorial de ", numero, " es 1.")
        else:
            numFactorial = 1
            for valor in range(1, numero+1, 1):
                numFactorial = numFactorial * valor
            print("El numero factorial de ", numero, "es ", numFactorial)
    if numero < 0:
        print("El numero es negativo")
    else:
        print("No has introducido un numero")

## CASOS TEST ##

# Si no es un numero
numero = "hola"
factorial(numero)

# Si el numero es negativo
numero = -8
factorial(numero)

# Si el numero es 0
numero = 0
factorial(numero)

# Si el numero es positivo
for numero in range(1, 11, 1):
    factorial(numero)