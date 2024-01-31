from .persona import Persona

class Candidato(Persona):
    def __init__(self, nombre, ci, fecha_nacimiento, genero, partido):
        super().__init__(nombre, ci, fecha_nacimiento, genero)
        self.__partido = partido
        self.__image_path = partido + '.jpg'

    @property
    def partido(self):
        return self.__partido

    @property
    def image_path(self):
        return self.__image_path