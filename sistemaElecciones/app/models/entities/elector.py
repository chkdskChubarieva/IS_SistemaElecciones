from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from .persona import Persona

class Elector(Persona, UserMixin):

    def __init__(self, nombre, ci, fecha_nacimiento, habilitado, genero): # aumentar fecha_nacimiento
        super().__init__(nombre, ci, fecha_nacimiento, genero) # aumentar fecha_nacimiento
        self.__habilitado = habilitado

    @property
    def habilitado(self):
        return self.__habilitado

    @habilitado.setter
    def habilitado(self, habilitado):
        self.__habilitado = habilitado

    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)
