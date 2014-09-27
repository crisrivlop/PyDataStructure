
#Clase Node, es un contenedor que las estructuras de datos, lineales y unidireciones
#pueden usar para almacenar datos. 
class Node():
    def __init__(self, data, pnext):
        #el dato contenido
        self.__data = data
        #el puntero al nodo siguiente
        self.__next = pnext
    def __str__(self):
        return str(self.__data)
    #setea el puntero al siguiente Nodo
    def setNext(self, pnext):
        self.__next = pnext
    #obtiene el nodo que sigue
    def getNext(self):
        return self.__next
    #setea el dato que el nodo contiene
    def setData(self, data):
        self.__data = data
    #obtiene el dato que el nodo contiene
    def getData(self):
        return self.__data