import numpy as np

class PilaSecuencial :
	__array : np.ndarray
	__tope : int
	__cant : int
	__max : int

	def __init__ (self, max = 0) :
		self.__array = np.empty(max, dtype=object)
		self.__tope = -1
		self.__cant = 0
		self.__max = max

	def vacia (self) :
		return self.__cant == 0

	def llena (self) :
		return self.__cant == self.__max

	def insertar (self, x) :
		if not self.llena() :
			self.__tope += 1
			self.__array[self.__tope] = x
			self.__cant += 1
			return x
		else :
			return 0

	def suprimir (self) :
		if self.vacia() :
			print ("Pila vacia")
			return 0
		else :
			x = self.__array[self.__tope]
			self.__tope -= 1
			self.__cant -= 1
			return x

	def recorrer (self) :
		if not self.vacia() :
			i = self.__tope
			j = 0
			while j < self.__cant :
				print (self.__array[i])
				i -= 1
				j += 1

