from Nodos import Nodo

class PilaEnlazada :
	__cant : int
	__tope : Nodo

	def __init__(self, tope = None, cant = 0) :
		self.__cant = cant
		self.__tope = tope

	def vacia (self) :
		return self.__cant == 0

	def insertar (self, x) :
		nuevo = Nodo(x)
		nuevo.setSig(self.__tope)
		self.__tope = nuevo
		self.__cant += 1
		return nuevo.getDato()

	def suprimir (self) :
		if self.vacia() :
			print ("Pila vacia")
			return 0
		else :
			x = self.__tope.getDato()
			self.__tope = self.__tope.getSig()
			self.__cant -= 1
			return x

	def muestraTope (self) :
		return self.__tope.getDato()

	def recuperarTope (self) :
		return self.__tope

	def recorrer (self) :
		if self.vacia() :
			print ("Pila vacia")
		else :
			aux = self.__tope
			while aux != None :
				print (aux.getDato())
				aux = aux.getSig()