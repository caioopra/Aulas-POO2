class Produto:
    """Insira aqui todos metodos e atributos ... """

    def __init__(self, codigo, descricao, categoria):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__categoria = categoria

    # getters
    @property
    def codigo(self):
        return self.__codigo

    @property
    def descricao(self):
        return self.__descricao

    @property
    def categoria(self):
        return self.__categoria

    @property
    def quantidade(self):
        return self.__quantidade

    @property
    def preco_unitario(self):
        return self.__preco_unitario

    @property
    def cliente(self):
        return self.__cliente

    # setters
    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @categoria.setter
    def categoria(self, categoria):
        self.__categoria = categoria

    @quantidade.setter
    def quantidade(self, quantidade):
        self.__quantidade = quantidade

    @preco_unitario.setter
    def preco_unitario(self, preco_unitario):
        self.__preco_unitario = preco_unitario

    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente

    def preco_total(self):
        return self.quantidade * self.preco_unitario
