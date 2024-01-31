
class Persona:
    def __init__(self, nombre, ci, fecha_nacimiento, genero): #aumentar fecha_nacimiento
        self.__nombre = nombre.title()
        self.id = ci
        self.__ci = ci
        self.__fecha_nacimiento = fecha_nacimiento
        self.__genero = genero
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def ci(self):
        return self.__ci
     
    @property
    def fecha_nacimiento(self):
        return self.__fecha_nacimiento
    
    @property
    def genero(self):
        return self.__genero