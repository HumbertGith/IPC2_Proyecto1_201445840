from nodos import Nodo_lectura


class Lista_lectura :

    cabeza = None
    cabeza: 'Nodo_lectura'
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
    def add(self, lectura): 
        
        recibido = Nodo_lectura(lectura)  #convertimos el nodo que se trae en un nodoPersona
        nuevo = Nodo_lectura(recibido.lectura)
        
        if self.esVacia(): 

            self.cabeza = recibido
           
            self.tamanio=self.tamanio+1
        elif self.encontrado(recibido.lectura.x, recibido.lectura.y) == False :

             aux = self.cabeza
             while (aux.getSiguiente() != None) :
                aux = aux.getSiguiente()
        
             aux.setSiguiente(nuevo)
            
             self.tamanio= self.tamanio+1
        
    def encontrado(self, e, e1):
        encontrar = False
        temp = self.cabeza
        while temp != None:
            if e==temp.lectura.x and e1==temp.lectura.y:
                encontrar = True
            temp = temp.getSiguiente()      
        return encontrar
    
    def  get(self, i):
        temp = self.cabeza
        for  j in range(i) :
            temp=temp.getSiguiente()
        
        return temp.lectura


    
    def listar(self) :
        s = ""
        
        aux=self.cabeza
        #Verifica si la lista contiene elementoa.
        
            #Crea una copia de la lista.
           
            #Posicion de los elementos de la lista.
            
            #Recorre la lista hasta el final.
        while aux != None:
                # Imprime en pantalla el valor del nodo.
                print(aux.lectura.x, aux.lectura.y)
                aux= aux.siguiente