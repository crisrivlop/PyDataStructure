from list.Node import Node


class QueueException():
    def __init__(self,message):
        self.__message = message
    def __str__(self):
        return self.__message

#Clase Queue, es una estructura de dato de control, de tipo FIFO
#First In, First Out. por su traduccion en espanol primero en entrar, primero en salir
class Queue():
    def __init__(self):
        self.__head = None
        self.__tail = None
    #Inserta un dato al final de la cola
    def enqueue(self,data):
        if (self.__head == None):
            self.__tail = self.__head = Node(data)
        else:
            insertionNode = Node(data,None)
            self.__tail.setNext(insertionNode)
            self.__tail = insertionNode
            
    #Obtiene el dato al inicio de la cola y lo borra de la misma
    def dequeue(self):
        if (self.__head == None):
            raise QueueException("Queue Empty!")
        outNode = self.__head
        self.__head = self.__head.getNext()
        return outNode.getData()
    #Retorna un valor de verdad, verdadero si la cola esta vacia
    #falso si la cola contiene algo
    def isEmpty(self):
        return self.__head == None
        
            