class Dni():
    def __init__(self, cadena = ""):
        self.dni  = cadena
        self.correcto = False

    def entradaDni(self, cadena):
        self.dni = cadena

    def getDni(self):
        return self.dni

    def esCorrecto(self, valor):
        self.correcto = valor

    def comprobarLongitud(self):
        return len(self.dni) == 9

    def comprobarNumero(self):
        return self.dni[:-1].isdigit()

    def comprobarLetra(self):
        return self.dni[-1].isupper() and not self.dni[-1].isdigit()



    def comprobarDni(self):
        if self.comprobarLongitud() and self.comprobarNumero() and self.comprobarLetra():
            self.esCorrecto(True)




if __name__ ==  '__main__':

    dni1 = Dni()

    dni1.entradaDni('12345678X')
    print(dni1.dni)
    dni1.comprobarDni()
    print(dni1.correcto)

    dni2 = Dni()
    dni2.entradaDni('A2345678X')
    print(dni2.dni)
    dni2.comprobarDni()
print(dni2.correcto)