class Conta:

    # Funçâo contrutora (controi um objeto)
    # Os atributos são as caracteristicas dadas a essa função construtora para criar um objeto.
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ... {}".format(self))
        self.__numero = numero  # Esses "__" dentro dos meus atributos são formas de coloca-los privados. Isso se chama
        self.__titular = titular  # incapsulamento
        self.__saldo = saldo
        self.__limite = limite


    # Esses aqui são os métodos.
    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_desponivel_para_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_desponivel_para_sacar

    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):  # get é para pegar o elemento
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):  # set é para definir o elemento
        self.__limite = limite

    @staticmethod  # metodo estatico
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}
    