class Nodo :
	__dato : object
	__sig :  Nodo

	def __init__(self, dato = None):
		self.__dato = dato
		self.__sig = None

	def getDato (self) :
		return self.__dato

	def getSig (self) :
		return self.__sig

	def setDato (self, x) :
		self.__dato = x

	def setSig (self, x) :
		self.__sig = x