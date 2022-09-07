from tkinter import messagebox
from lista_celulas import Lista_celulas
from lista_lectura import Lista_lectura
from paciente import Paciente

#from paciente import Paciente



class Nodo_paciente(Paciente):
    siguiente: 'Nodo_paciente'
    paciente: 'Paciente'

    #lista_celulas: 'Lista_celulas'
    def __init__(self, paciente):    
        self.paciente=paciente
        self.siguiente=None
        self.lista_celulas=Lista_celulas()
        self.lista_le=Lista_lectura()
      
       
    def  getSiguiente(self):
          return self.siguiente 
    def setSiguiente(self, siguiente):
          self.siguiente = siguiente
    def getPaciente(self) :
        return self.paciente
    
class Lista_pacientes :

    listar_celulas:'Lista_celulas'
    cabeza=None
    cabeza:'Nodo_paciente'
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
    def add(self, paciente): 
        
        recibido = Nodo_paciente(paciente)  #convertimos el nodo que se trae en un nodoPersona
        nuevo = Nodo_paciente(recibido.paciente)
        nuevo.lista_celulas=recibido.lista_celulas
        nuevo.lista_le=recibido.lista_le
 
        if self.esVacia(): 

            self.cabeza = recibido
            messagebox.showinfo("info", "Se agrego correctamente el paciente")
            self.tamanio=self.tamanio+1
        elif self.encontrado(recibido.paciente.nombre) == False :

             aux = self.cabeza
             while (aux.getSiguiente() != None) :
                aux = aux.getSiguiente()
        
             aux.setSiguiente(nuevo)
             messagebox.showinfo("info", "Se agrego correctamente el paciente")
             self.tamanio= self.tamanio+1
    #encontrar de tipo boleano    
    def encontrado(self, e):
       try: 
         
        encontrar = False
        temp = self.cabeza
        while temp != None:
            if e==temp.nombre :
                encontrar = True
            temp = temp.getSiguiente()      
        return encontrar


       except:
        print("algo")

        

    def find(self, e) :
          NombreBuscado=e #debido a que el nombre viene de tipo objeto, es necesario pasarlo a String
          aux=self.cabeza
          while aux!=None:
                #Se comparan los nombres para ver si existe
                if(aux.paciente.nombre==NombreBuscado):
                    return aux;   #si es la persona que buscamos se retorna el nodo
                    print("encontrado")
                else:
                    aux=aux.getSiguiente(); 
                
            
          return None #si no se encuentra se devuelve null
    
    def listar(self) :
        cadena = ""
        nombre=""
        edad=""
        periodo=""
        tamanio=""
        #aux:'Nodo_paciente'
        aux=self.cabeza
        #Verifica si la lista contiene elementoa.
        
            #Crea una copia de la lista.
           
            #Posicion de los elementos de la lista.
            
            #Recorre la lista hasta el final.
        while aux != None:
                # Imprime en pantalla el valor del nodo.
                nombre=aux.paciente.nombre
                edad=str(aux.paciente.edad)
                periodo=str(aux.paciente.periodo)
                tamanio=str(aux.paciente.tamanioM)
                cadena=cadena+nombre+"  Edad: "+edad+" Periodos: "+periodo+ " Tamaño de musestra: "+tamanio+"\n"
                aux= aux.siguiente
        return cadena
                

    def listar_celulas(self) :
        s = ""
        aux=self.cabeza
        #Verifica si la lista contiene elementoa.
        
            #Crea una copia de la lista.
           
            #Posicion de los elementos de la lista.
            
            #Recorre la lista hasta el final.
        while aux != None:
                # Imprime en pantalla el valor del nodo.
                aux.lista_celulas.listar()
                aux= aux.siguiente