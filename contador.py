from cgitb import reset


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

    def reset(self):
        return self.get_vInicial()

    def incrementador(self):
        contador = self.get_vInicial()
        incremento = self.get_incremento()
        limite = self.get_limite()

        bucle = True

        while bucle:
            if (contador < limite):
                print(f'valor actual: {contador}')
                contador += incremento
            else:
                print('Se superó el límite\n')
                contador = self.reset()
                bucle = False
                return contador

if __name__ == '__main__':
    contador = Contador(0, 4, 16)
    contador.incrementador()
