from list.Node import Node

"""
Clase StackException
Esta clase soporta a la clase Stack, esta sirve para proporcionar el error
de una pila o Stack vacia
"""
class __StackException():
    def __init__(self,message):
        self.__message = message
    def __str__(self):
        return repr(self.__message)


#clase Stack representa una pila, o sea una estructura de datos
#del tipo LIFO Last In, First Out. 
#por su traduccion en espanol Ultimo en entrar, primero en salir
class Stack():

    def __init__(self):
        #el atributo cima, es una referencia al objeto que esta en la parte mas alta de la pila
        self.__top = None
    def __str__(self):
        out = "[" + self.__printNext(self.__top) + "]"
        return out
    def __printNext(self,node):
        if (node.getNext() != None):
            return node.__str__() + "," + self.__printNext(node.getNext()).__str__()
        return node.__str__()
    #Metodo push(data) agrega un objeto en la cima de la pila
    def push(self,data):
        self.__top = Node(data, self.__top)
    #Metodo pop() quita el objeto en la cima de la pila y el siguiente objeto
    #si es que lo hay se convierte en la cima de la pila
    def pop(self):
        if (self.__top == None):
            raise __StackException("Empty Stack!")
        data = self.__top
        self.__top = self.__top.getNext()
        return data.getData()
    #Obtiene el dato que esta en la cima de la pila sin alterar esta
    def peek(self):
        if (self.__top != None):
            return self.__top.getData()
        raise __StackException("Empty Stack!")
    #Se retorna un valor de verdad, verdadero si la pila esta vacia y falso si no lo esta
    def isEmpty(self):
        return self.__top == None
            