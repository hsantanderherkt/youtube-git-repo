# GRUPO 2:
# Enzo Cortez
# Karen Bonilla
# Héctor Santander

import time
import os

class cVehiculo:
    __marca=""
    __modelo=""
    __color=""
    __llantas=0
    __puertas=0
    
    def __init__(self,marca,modelo,color,llantas,puertas):
        self.__marca=marca
        self.__modelo=modelo
        self.__color=color
        self.__llantas=llantas
        self.__puertas=puertas
    
    def getMarca(self):
        return(self.__marca)
    def getModelo(self):
        return(self.__modelo)
    def getColor(self):
        return(self.__color)
    def getLlantas(self):
        return(self.__llantas)
    def getPuertas(self):
        return(self.__puertas)
    
    def setMarca(self,marca):
        self.__marca=marca
    def setModelo(self,modelo):
        self.__modelo=modelo
    def setColor(self,color):
        self.__color=color
    def setMLlantas(self,llantas):
        self.__llantas=llantas
    def setPuertas(self,puertas):
        self.__puertas=puertas
    
    def mostrarDatosVehiculo(self):
        print("Marca: ",self.__marca)
        print("Modelo: ",self.__modelo)
        print("Color: ",self.__color)
        print("Llantas: ",self.__llantas)
        print("Puertas: ",self.__puertas)

    def encender(self):
        print("El auto se ha encendido")
    
    def apagar(self):
        print("El auto se ha apagado")
    
    def acelerar(self,velocidad):
        for i in range(0,velocidad,2):
            print("El auto está acelerando a una velocidad de:",i," Km/h")
            time.sleep(0.5)
        print("El auto llegó a la velocidad de:",velocidad," Km/h")
    
    def frenar(self,velocidad,frenado):
        for i in range(velocidad,frenado,-2):
            print("El auto está frenando...el odómetro marca:",i," Km/h")
            time.sleep(0.5)
        print("El auto bajó a la velocidad de:",frenado," Km/h")
    
class cConductor:
    __nombre=""
    __experiencia=0
    
    def __init__(self,nombre,experiencia):
        self.__nombre=nombre
        self.__experiencia=experiencia
    
    def getNombre(self):
        return(self.__nombre)
    def getAniosExp(self):
        return(self.__experiencia)
    def setNombre(self,nombre):
        self.__nombre=nombre
    def setAniosExp(self,experiencia):
        self.__experiencia=experiencia
    
    def mostrarDatosConductor(self):
        print("Nombre: ",self.__nombre)
        print("Experiencia: ",self.__experiencia," años")
    
    def empezarManejo(self):
        print("{} ha empezado a manejar".format(self.__nombre))
    
    def terminarManejo(self):
        print("{} ha terminado de manejar".format(self.__nombre))

# Creación de objetos para cada instancia de clase
oCarro1=cVehiculo("Nissan","Maxima","Rojo",4,4)
oChofer1=cConductor("Enzo Cortez",15)

# Método para el menú de opciones
def menu():
    os.system("cls") # Limpia la pantalla
    print("<<<<<------SISTEMA DE MANEJO------>>>>>")
    print("")
    print("\t<1> - Mostrar datos del vehículo")
    print("\t<2> - Mostrar datos del conductor")
    print("\t<3> - Encender vehículo")
    print("\t<4> - Empezar a manejar")
    print("\t<5> - Acelerar vehículo")
    print("\t<6> - Frenar vehículo")
    print("\t<7> - Aapagar vehículo")
    print("\t<8> - Terminar la conducción")
    print("\t<9> - Salir")
while True:
    # Mostramos el menu
    menu()
    # solicituamos una opción al usuario
    opcionMenu = input("Escoga una opción >> ")
    if opcionMenu=="1":
        print ("")
        oCarro1.mostrarDatosVehiculo()
        input("\npulse una tecla para continuar")
    elif opcionMenu=="2":
        print ("")
        oChofer1.mostrarDatosConductor()
        input("\npulse una tecla para continuar")
    elif opcionMenu=="3":
        print ("")
        oCarro1.encender()
        input("\npulse una tecla para continuar")
    elif opcionMenu=="4":
        print ("")
        oChofer1.empezarManejo()
        input("\npulse una tecla para continuar")
    elif opcionMenu=="5":
        print ("")
        oCarro1.acelerar(10)
        input("\npulse una tecla para continuar")
    elif opcionMenu=="6":
        print ("")
        oCarro1.frenar(10,2)
        input("\npulse una tecla para continuar")
    elif opcionMenu=="7":
        print ("")
        oCarro1.apagar()
        input("\npulse una tecla para continuar")
    elif opcionMenu=="8":
        print ("")
        oChofer1.terminarManejo()
        input("\npulse una tecla para continuar")
    elif opcionMenu=="9":
        break
    else:
        print ("")
        input("No has pulsado ninguna opción correcta...\npulse una tecla para continuar")
