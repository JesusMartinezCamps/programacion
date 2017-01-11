#Calcular area de un rectangulo y el perimetro exterior en metros cuadrados
print("Introduce la base del rectangulo que quieres calcular:")
base = input()
print("Introduce la altura del rectangulo que quieres calcular:")
altura = input()

area = base * altura 
perimetro = 2 * base + 2 * altura

print("El area es:", area, "y el perimetro es:", perimetro)