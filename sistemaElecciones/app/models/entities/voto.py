class Voto:
    def __init__(self, elector, voto): #voto - nombre partido
        self.__elector = elector
        self.__voto = voto

    @property
    def voto(self):
        return self.__voto

    def emitir_voto(self):
        if self.__elector.habilitado == 1:
            self.__elector.habilitado = 0
        else:
            print('Usted {} ya realizó su voto ... estado habilitación:{}'.format(self.__elector.nombre, 'inhabilitado'))
            