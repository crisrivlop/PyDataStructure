from Node import Node


class IndexOutBound():
    def __init__(self, index):
        self.__index = index
    def __str__(self):
        return "Index out bound: " + str(self.__index)

class ErrorToCast():
    def __init__(self,pobject, ptype):
        self.__object = pobject
        self.__type = ptype
    def __str__(self):
        return "error: the object" + object.__str__() + "isn`t type" + type.__str__()


#Clase List, es una estructura de datos
#List es una Lista enlazada simple
class List():
    
    #metodo constructor
    def __init__(self):
        #es el puntero inicial de la lista
        self.__head = None
        #es el puntero final de la lista
        self.__tail = None
        #es el largo de la lista representado por un numero
        self.__lenght = 0
    
    
    def __str__(self):
        actualNode = self.__head
        out = "["
        i = 0
        while (i < self.__lenght-1):
            out += actualNode.__str__() + ","
            actualNode = actualNode.getNext()
            i+=1
        out += actualNode.__str__() + "]"
        return out 
    
    
    
    #addi. inserta un dato al principio de la lista e incrementa el largo de la lista en uno
    def addi(self,data):
        if (self.__head == None):
            self.__head = self.__tail = Node(data,None)
        else:
            insertionNode = Node(data,self.__head)
            self.__head = insertionNode
        self.__lenght += 1
    
    
    
    #addf. inserta un dato al final de la lista e incrementa el largo de la lista en uno
    def addf(self,data):
        if (self.__head == None):
            self.__head = self.__tail = Node(data,None)
        else:
            insertionNode = Node(data,None)
            self.__tail.setNext(insertionNode)
            self.__tail = insertionNode
        self.__lenght += 1 
    
    
    #add. inserta el dato en la posicion indicada por el parametro index
    #index tiene que ser un numero entero, ademas tiene que estar entre los valores de
    #0 hasta el largo de la lista
    def add(self,data,index):
        if (index == 0):
                self.addi(data)
        elif (index == self.__lenght):
            self.add(data)
        else:
            previousNode = self.__getNodeByIndex(index-1)
            insertionNode = Node(data, previousNode.getNext())
            previousNode.setNext(insertionNode)
            self.__lenght += 1
   
    
    #obtiene el nodo en la posicion dada por el parametro index
    #ademas index debe ser un numero entero, que tiene los valores en el intervalo 
    #[0, largo de la lista -1] 
    def __getNodeByIndex(self,index):
        if (not isinstance(index, int)):
            raise ErrorToCast(index, "int")
        elif (0 <= index and index < self.__lenght):
            actualNode = self.__head
            i = 0
            while (i < index):
                actualNode = actualNode.getNext()
                i += 1
            return actualNode
        else:
            raise IndexOutBound(index)
    
    
    #Remueve el primer dato de la lista, actualizando el largo de la lista
    def __removeFirst(self):
        if (self.__lenght == 1):
            self.__head = self.__tail = None
        else:
            self.__head = self.__head.getNext()
        self.__lenght += -1
        
        
    #Remueve el ultimo dato de la lista, actualizando el largo de la lista
    def __removeLast(self):
        if (self.__lenght == 1):
            self.__head = self.__tail = None
        else:
            self.__tail = self.__getNodeByIndex(self.__lenght - 2)
            self.__tail.setNext(None)
        self.__lenght +=-1
        
    
    
    #Remueve el dato en la posicion indicada por el parametro index
    #este debe ser un numero entero ademas debe de estar entre el intervalo   
    #[0, largo de la lista -1]  
    def remove(self,index):
        if (0 > index or index >= self.__lenght):
            raise IndexOutBound(index)
        if (index == 0):
            self.__removeFirst()
        elif(index == 1):
            self.__removeLast()
        else:
            previousNode = self.__getNodeByIndex(index-1)
            previousNode.setNext(previousNode.getNext().getNext())
            self.__lenght -= 1
    
    
    #retorna el largo de la lista representado por un numero entero
    def getLenght(self):
        return self.__lenght
    
    #retorna un valor de verdad, si la lista esta vacia 
    #retorna verdadero y falso si no lo esta
    def isEmpty(self):
        return self.__lenght == 0
    
    #obtiene un dato en la posicion indicada por el parametro index
    #este debe ser un numero entero ademas debe de estar entre el intervalo   
    #[0, largo de la lista -1]  
    def get(self,index):
        return self.__getNodeByIndex(index).getData()
    
    #setea el dato en la posicion indicada por el parametro index
    #este debe ser un numero entero ademas debe de estar entre el intervalo   
    #[0, largo de la lista -1]
    def set(self,index,newData):
        self.__getNodeByIndex(index).setData(newData)