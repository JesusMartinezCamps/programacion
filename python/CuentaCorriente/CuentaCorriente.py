class CuentaCorriente:
	def __init__ (self, nombre, apellido, telefono, direccion, nif, saldo):
		self.nombre = nombre
		self.apellido = apellido
		self.telefono = telefono
		self.direccion = direccion
		self.nif = nif
		self.saldo = saldo

	#get y set de los parametros

	#De nombre
	def getNombre(self):
		return self.nombre

	def setNombre(self, nombre):
		print("Introcude el nombre: ")
		nombre = input()
		print("Se ha introducido: ", nombre)
		self.nombre = nombre

	#De apellido
	def getApellido(self):
		return self.apellido

	def setApellido(self, apellido):
		print("Introcude el apellido: ")
		apellido = input()
		print("Se ha introducido: ", apellido)
		self.apellido = apellido

	#De telefono
	def getTelefono(self):
		return self.telefono

	def setTelefono(self, telefono):
		self.telefono = telefono

	#De direccion
	def getDireccion(self):
		return self.direccion

	def setDireccion(self, direccion):
		self.direccion = direccion

	#De NIF
	def getNif(self):
		return self.nif

	def setNif(self, nif):
		self.nif = nif

	#De saldo
	def getSaldo(self):
		return self.saldo

	def setSaldo(self, saldo):
		self.saldo = saldo


	#Metodos modificar la cuenta
	def consultarCuenta(self):
		print("Nombre: ",self.nombre,"Apellidos: ",self.apellido,"Telefono: ",self.telefono, "Direccion: ",self.direccion,"NIF: ",self.nif,"Saldo: ",self.saldo,"euros")

	def retirarDinero(self, retirada):
		self.saldo = self.saldo - retirada

	def ingresarDinero(self,ingreso):
		
		
		self.saldo = self.saldo + ingreso
		print("Tu saldo actual es"+ingreso)

	def estadoSaldo(self):
		if self.saldo < 0:
			print("Tu saldo es negativo")
			return True
		else:
			print("Tu saldo es positivo")
			return False


#Prueba:
if __name__ == "__main__":
	
	cuentaCorrienteEjemplo = CuentaCorriente("Antonio","Perez","65235971","Avenida","4565125B",20)
	
	cuentaCorrienteEjemplo.setNombre()
