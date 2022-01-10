class cPais:
    __nombre=""
    __habitantes=0
    
    def __init__(self,n,h):
        self.__nombre=n
        self.__habitantes=h
    
    def getNombre(self):
        return(self.__nombre)
    
    def getHabitantes(self):
        return(self.__habitantes)
    
    def setNombre(self,n):
        self.__nombre=n
    
    def setHabitantes(self,h):
        self.__habitantes=h
    
oPais1=cPais("Alemania",2500000)
oPais2=cPais("Ecuador",1500000)
oPais3=cPais("Brasil",18000000)

print("El país posee el número de habitantes:")
print(oPais1.getHabitantes())
print(oPais1.getNombre())

oPais1.setNombre("NOMBRE NUEVO")
print(oPais1.getNombre())