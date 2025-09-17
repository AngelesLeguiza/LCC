from Nodos import Nodo

class ColaEnlazada :
	__cant : int
	__primero : Nodo
	__ultimo : Nodo

	def __init__(self, prim = None, ult = None, cant = 0) :
		self.__cant = cant
		self.__primero = prim
		self.__ultimo = ult

	def vacia (self) :
		return self.__cant == 0

	def insertar (self, x) :
		nuevo = Nodo(x)
		if self.__ultimo == None :
			self.__primero = nuevo
		else :
			self.__ultimo.setSig(nuevo)
		self.__ultimo = nuevo
		self.__cant += 1
		return self.__ultimo.getDato()

	def suprimir (self) :
		if self.vacia() :
			print ("Cola vacia")
			return 0
		else :
			x = self.__primero.getDato()
			self.__primero = self.__primero.getSig()
			self.__cant -= 1
			if self.vacia() :
				self.__fondo = None
			return x

	def muestraPrimero (self) :
		return self.__primero.getDato()

	def recuperarPrimero (self) :
		return self.__primero

	def recorrer (self) :
		aux = self.__primero
		while aux != None :
			print (aux.getDato())
			aux = aux.getSig()
