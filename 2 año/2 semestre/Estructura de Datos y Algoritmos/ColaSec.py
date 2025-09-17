import numpy as np

class ColaSecuencial:
	__array : np.ndarray
	__primero : int
	__ultimo : int
	__cant : int
	__max : int

	def __init__ (self, max = 0) :
		self.__array = np.empty(max, dtype=object)
		self.__primero = 0
		self.__ultimo = 0
		self.__cant = 0
		self.__max = max

	def vacia (self) :
		return self.__cant == 0

	def llena (self) :
		return self.__cant == self.__max

	def insertar (self, x) :
		if not self.llena() :
			self.__array[self.__ultimo] = x
			self.__ultimo = (self.__ultimo + 1) % self.__max
			self.__cant += 1
			return x
		else :
			return 0

	def suprimir (self) :
		if self.vacia() :
			print ("Cola vacia")
			return 0
		else :
			x = self.__array[self.__primero]
			self.__primero = (self.__primero + 1) % self.__max
			self.__cant -= 1
			return x

	def recorrer (self) :
		if not self.vacia() :
			i = self.__primero
			j = 0
			while j < self.__cant :
				print (self.__array[i])
				i = (i + 1) % self.__max
				j += 1
