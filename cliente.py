class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    @property  # serve para nao precisar colocar os parenteses, é uma sintaxe para um getter
    def nome(self):
        return self.__nome.title()  # .title faz com q a primeira letra do elemento seja maiúscula

    @nome.setter
    def nome(self, nome):
        self.__nome = nome