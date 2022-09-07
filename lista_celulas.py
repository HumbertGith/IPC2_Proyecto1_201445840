#from celulas import Celula
from nodos import Nodo_celula


class Lista_celulas :

    
    cabeza=None
    cabeza: 'Nodo_celula'
    tamanio=0

    def __init__  (self): 
        cabeza = None
        tamanio = 0
    

    def getTamanio(self): 
        return self.tamanio
    

    def setTamanio(self, tamanio): 
        self.tamanio = tamanio
    

    def esVacia(self): 
        return self.cabeza == None
#agrega una celula a la lista
    def add(self, celula): 
        
        recibido = Nodo_celula(celula)  #convertimos el nodo que se trae en un nodoPersona
        nuevo = Nodo_celula(recibido.celula)
        
        if self.esVacia(): 

            self.cabeza = recibido
            self.tamanio=self.tamanio+1
        elif self.encontrado(recibido.celula.x, recibido.celula.y) == False :

             aux = self.cabeza
             while (aux.getSiguiente() != None) :
                aux = aux.getSiguiente()
        
             aux.setSiguiente(nuevo)
             self.tamanio= self.tamanio+1
        
    def encontrado(self, e, e1):
        encontrar = False
        temp = self.cabeza
        while temp != None:
            if e==temp.celula.x and e1==temp.celula.y:
                encontrar = True
            temp = temp.getSiguiente()      
        return encontrar
    def find(self, e, e1) :
          NombreBuscado=e #debido a que el nombre viene de tipo objeto, es necesario pasarlo a String
          aux=self.cabeza
          while aux!=None:
                #Se comparan los nombres para ver si existe
                if(aux.celula.x==NombreBuscado and aux.celula.y==e1):
                    return aux.celula;   #si es la persona que buscamos se retorna el nodo
                   
                else:
                    aux=aux.getSiguiente(); 
                
            
          return None #si no se encuentra se devuelve null
    def listar(self) :
        s = ""
        #aux:'Nodo_celula'
        aux=self.cabeza
        #Verifica si la lista contiene elementoa.
        
            #Crea una copia de la lista.
           
            #Posicion de los elementos de la lista.
            
            #Recorre la lista hasta el final.
        while aux != None:
                # Imprime en pantalla el valor del nodo.
                
                print(aux.celula.enferma, aux.celula.x, aux.celula.y, aux.celula.posicion)
                aux= aux.siguiente
    def listarV(self):
        aux=self.cabeza
        while aux!=None:
            aux.celula.obtenerVecinos()
            aux=aux.siguiente
    def  get(self, i):
        temp = self.cabeza
        for  j in range(i) :
            temp=temp.getSiguiente()
        
        return temp.celula
         