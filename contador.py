class Contador():
    
    def __init__(self, vInicial=0, incremento=1, limite=None):

        self.__vInicial = vInicial
        self.__incremento = incremento
        self.__limite = limite

    def get_vInicial(self):
        return self.__vInicial

    def get_incremento(self):
        return self.__incremento

    def get_limite(self):
        return self.__limite