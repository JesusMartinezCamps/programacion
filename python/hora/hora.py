# coding = utf-8

class Hora:
	def __init__(self, hora=0, minutos=0, segundos=0):
		self.hora = hora
		self.minutos = minutos
		self.segundos = segundos

	def __repr__(self):
		return self.hora + ":" + self.minutos + ":" + self.segundos

	def setHora(self, hora):
		self.hora = hora

	def getHora(self, hora):
		return self.hora

	def setMinutos(self, minutos):
		self.minutos = minutos

	def getMinutos(self, minutos):
		return self.minutos

	def setSegundos(self, segundos):
		self.segundos = segundos

	def getSegundos(self, segundos):
		return self.segundos

	def devolverHora(self):
		return self.hora + ":" + self.minutos + ":" + self.segundos

def introducirHora():
	horaActual = input("Hora: ")
	minutosActual = input("Minutos: ")
	segundosActual = input("Segundos: ")
	hora = Hora(horaActual, minutosActual, segundosActual)
	hora.devolverHora()

introducirHora()