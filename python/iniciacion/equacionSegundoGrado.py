# Equacion de segundo grado: ax^2 + bx + c = 0

def equacionSegundoGrado(a, b, c):

	import math

	discriminante = b**2 - 4*a*c

	if a != 0 and discriminante >= 0:
		resultadoRaizCuadrada = math.sqrt(discriminante)

		x1 = (-b + resultadoRaizCuadrada) / (2 * a)
		x2 = (-b - resultadoRaizCuadrada) / (2 * a)

		return x1, x2

	else:
		return None

# casos test
a = -1
b = -2
c = -1

#si a = 0 => no existe solucion real
a = 0
b = -2
c = -1

if None == equacionSegundoGrado(a, b, c):
	print("PASS a = 0")
else:
	print("FAIL a = 0")

# si b = 0 y -c/a < 0 => no existe solucion real
a = -1
b = 0
c = -1
if None == equacionSegundoGrado(a, b, c):
	print("PASS a = 0 AND -c/a < 0")
else:
	print("FAIL a =0 AND -c/a < 0")


# si b = 0 y c = 0 => x1 = x2 = 0
a = -1
b =  0
c =  0
x1, x2 = equacionSegundoGrado(a, b, c)
if x1 == 0 and x2 == 0:
    print("PASS b = 0 y c = 0")
else:
	print("FAIL b = 0 y c = 0")


# si c = 0 => x1 = 0 and x2 = -b/a
a = -1
b = -2
c =  0
desviacion = 0.01
x1, x2 = equacionSegundoGrado(a, b, c)

if b > 0:
	raizNula   = x1
	raizNoNula = x2
else:
	raizNula   = x2
	raizNoNula = x1


# esto seria depuracion
if raizNula == 0 and -b/a + desviacion >= raizNoNula >= -b/a - desviacion :  
	print("PASS c = 0")
else:
	print("FAIL c = 0") 
