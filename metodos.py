from gzip import WRITE
from re import L
from xml.dom import minidom
import xml.etree.ElementTree as ET
from celulas import Celula, Coordenada_lectura
from lista_pacientes import Nodo_paciente

from paciente import Paciente


class metodos:
    def __init__(self) -> None:
        pass
 
    #lee el archivo xml y llena las estructuras de datos
    def leer_archivo(lista, archivo ):
        with open(archivo, encoding='utf-8') as file:
            
            if file.readable():
                xml_data= ET.fromstring(file.read())
                lst_pa= xml_data.findall('paciente')
                for paciente in lst_pa:
                    lista2=""
                    lista3=""
                    lista2=paciente.find('periodos').text
                    
                    lista3=paciente.find('m').text
                    
                    lista1=paciente.findall('datospersonales')
                    nombre=""
                    nombret=""
                    edat=""
                    for elemt in lista1:
                        
                        nombre =elemt.find('nombre').text.split('$')
                        nombret=nombre[0]
                        
                        edad=elemt.find('edad').text.split('$')
                        edat=edad[0]
                        pacient=Paciente(nombret,int(edat), int(lista2),int(lista3))

                        lista.add(pacient)
                        
                        
                        
                    lista4=paciente.findall('rejilla')

                    for element in lista4:
                        celda=element.findall('celda')
                        for c in celda:
                            listav=[]
                            celda1=c.attrib.values()
                            x1=""
                            for x in celda1:
                                x1=x+","+x1
                            x2=x1.split(',')
                            f=x2[1]
                            c=x2[0]
                            encontrado:'Nodo_paciente'
                            encontrado=lista.find(pacient.nombre)
                            if encontrado != None:
                                lec=Coordenada_lectura(int(f),int(c))
                                encontrado.lista_le.add(lec)
             
            else:
                print(False)
    #metodo que crea la puestra de inicio del paciente
    def crear_muestra(lista, nombre):
            m=0
            
            encontrado:'Nodo_paciente'
            encontrado=lista.find(nombre)
            if encontrado != None:
                
                m=encontrado.paciente.tamanioM
                
                zize=0

                for  y in range(0,m): 
                    for x in range(0,m):
                        
                        encontrado.lista_celulas.add(Celula(False, x, y, zize))
                        zize=zize+1
               
                ran=encontrado.lista_le.tamanio
                
                for  i in range(ran):
                    clase=encontrado.lista_le.get(i)
                    celula=encontrado.lista_celulas.find(clase.x, clase.y)
                    celula.enfermar()
     #mtodo que sna todas las celulas de la muestra del paciente           
    def limpiar_muestra(lista, nombre):
            m=0
            
            encontrado:'Nodo_paciente'
            encontrado=lista.find(nombre)
            if encontrado != None:
                
                m=encontrado.paciente.tamanioM
                
                zize=0

                for  i in range(encontrado.lista_celulas.tamanio): 
                    celula=encontrado.lista_celulas.get(i)
                    celula.sanar()
    #metodo de devuelve una cadena para mostrar de forma grafica a las muestras         
    def mostrar_muestra(lista, nombre):
         
        encontrado:'Nodo_paciente'
        encontrado=lista.find(nombre)
        if encontrado != None:
                tam= encontrado.lista_celulas.tamanio
                m=encontrado.paciente.tamanioM
                grafico=""
                for i in range(tam):
                            cel=encontrado.lista_celulas.get(i)
                            reprentacion="|░|"
                            salto='\n'
                            
                            if cel.enferma:
                                reprentacion="|█|"
                            if cel.x==m-1:
                                
                                grafico=grafico + reprentacion+salto
                            else:
                                grafico=grafico+reprentacion
                return grafico
    #metodo de se encarga del algoritmo de enfermar a las celulas
    def seguirEnferma(muestra, vecinos, m): 

        vecinosEnfermos = 0
        for vecino in vecinos:
            if (vecino.x >= 0 and vecino.x < m) and (vecino.y >= 0 and vecino.y < m): 
                posicion = vecino.x + vecino.y * m
                celula = muestra.get(posicion)
                if celula.enferma: 

                    vecinosEnfermos+=1
                
            
        
        if vecinosEnfermos == 2 or vecinosEnfermos == 3:
            return True
        
        return False
    #metodo que se encarga de enfermar a las celulas
    def enfermarCelula(muestra, vecinos, m) :
        vecinosEnfermos = 0
        for vecino in vecinos :


            if (vecino.x >= 0 and vecino.x < m) and (vecino.y >= 0 and vecino.y < m):
                posicion = vecino.x + vecino.y * m

                celula = muestra.get(posicion)
                if (celula.enferma): 

                    vecinosEnfermos+=1
                
            
        
        if (vecinosEnfermos == 3): 
            return True
        
        return False
    #metodo  que se encarga de generar nuevos patrones
    def nuevaMuestra(lista, nombre) :
        celulasEnfermas = []

        encontrado:'Nodo_paciente'
        encontrado=lista.find(nombre)
        #ceulas=encontrado.lista_celulas
        #encontrado.paciente.listaCe2.append(ceulas)
                
       
        if encontrado != None:
                tam= encontrado.lista_celulas.tamanio
                m=encontrado.paciente.tamanioM
               
                for i in range(tam):
                    #Analizamos las celulas
                    celula=encontrado.lista_celulas.get(i)
                    if celula.enferma :
                        vecinos = celula.obtenerVecinos()

                        if metodos.seguirEnferma(encontrado.lista_celulas, vecinos, m):
                            celulasEnfermas.append(celula.posicion)
                        

                    else: 
                        vecinos = celula.obtenerVecinos()
                        if metodos.enfermarCelula(encontrado.lista_celulas, vecinos,m):
                            celulasEnfermas.append(celula.posicion)
                        
                    
                for  i in range(tam): 
                    celula1=encontrado.lista_celulas.get(i)
                    celula1.sanar()
                
                for celula in celulasEnfermas:
                    cel = encontrado.lista_celulas.get(celula)
                    cel.enfermar()
               

            
            
            
                
                        
               
    #metodo que se encarga de analizar y validar cada nuevo patron          
    def analizar(lista, nombre):
 
        metodos.nuevaMuestra(lista,nombre)
        cadena=metodos.mostrar_muestra(lista, nombre)
        return cadena
    #metodo que se encarga de generar el xml de cada paciente  
    def escribir_xml( lista, nombre, ruta):
        encontrado:'Nodo_paciente'
        encontrado=lista.find(nombre)
        if encontrado != None:
            elemento_1 = ET.Element('pacientes')
            elemento_hijo_1 = ET.SubElement(elemento_1, 'paciente')
            elemnto_paciente1=ET.SubElement(elemento_hijo_1, 'datospersonales')
            datos_personales_hijo1=ET.SubElement(elemnto_paciente1, 'nombre')
            datos_personales_hijo1.text=encontrado.paciente.nombre
            datos_personales_hijo2=ET.SubElement(elemnto_paciente1, 'edad')
            datos_personales_hijo2.text=str(encontrado.paciente.edad)
            elemnto_paciente2=ET.SubElement(elemento_hijo_1, 'periodos')
            elemnto_paciente2.text=str(encontrado.paciente.periodo)
            elemnto_paciente3=ET.SubElement(elemento_hijo_1, 'm')
            elemnto_paciente3.text=str(encontrado.paciente.tamanioM)
            elemnto_paciente4=ET.SubElement(elemento_hijo_1, 'resultado')
            elemnto_paciente4.text=str(encontrado.paciente.estado1)
            elemnto_paciente5=ET.SubElement(elemento_hijo_1, 'n')
            elemnto_paciente5.text=str(encontrado.paciente.n)
            elemnto_paciente6=ET.SubElement(elemento_hijo_1, 'n1')
            elemnto_paciente6.text=str(encontrado.paciente.n1)
            rough_string = ET.tostring(elemento_1, 'utf-8').decode('utf8')
            reparsed = minidom.parseString(rough_string)
            cadena=reparsed.toprettyxml(indent="  ")
            ruta.write(cadena)
            ruta.close()

    
       
   # metodo que se  encarga de diagnosticar los pacientes
    def mostrar_lista_celulas(lista, nombre):
       
        encontrado:'Nodo_paciente'
        encontrado=lista.find(nombre)
        tam= encontrado.lista_celulas.tamanio
        m=encontrado.paciente.tamanioM
        cont=1
        esigual=False
        if encontrado != None:
           
            for num, celula in enumerate(encontrado.paciente.listaCe):
                for celula2 in encontrado.paciente.listaCe[num +1:]:
                    if celula==celula2:
                       esigual=True
                       break
                    else:
                       esigual==False
                       cont+=1
                
                if esigual==True:
                    break
                
                   
                   
            
            if esigual==True and (cont>1 and cont< len(encontrado.paciente.listaCe)):
               encontrado.paciente.estado1="Grave"
               encontrado.paciente.n=cont
            elif esigual==True and cont==1:
               encontrado.paciente.estado1="Mortal"
               encontrado.paciente.n=1
            else :
               encontrado.paciente.estado1="Leve"
           
                    
                        
                
            
                
                