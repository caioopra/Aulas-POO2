from abstractControladorChamados import AbstractControladorChamados
from tipoChamado import TipoChamado
from chamado import Chamado
from datetime import date as Date
from cliente import Cliente
from tecnico import Tecnico
from collections import defaultdict


class ControladorChamados(AbstractControladorChamados):
    def __init__(self):
        self.__tipoChamados = []
        self.__listaChamados = []

    @property
    def tipoChamados(self):
        return self.__tipoChamados

    def totalChamadosPorTipo(self, tipo: TipoChamado) -> int:
        if self.__listaChamados == []:
            return 0
        else:
            count = 0
            for chamado in self.__listaChamados:
                if chamado.tipo == tipo:
                    count += 1
            return count

    def incluiChamado(self, data: Date, cliente: Cliente, tecnico: Tecnico, titulo: str, descricao: str,
                      prioridade: int, tipo: TipoChamado) -> Chamado:
        if self.__listaChamados == []:
                novoChamado = Chamado(data, cliente, tecnico, titulo,
                                      descricao, prioridade, tipo)
                self.__listaChamados.append(novoChamado)

                return novoChamado        
        else:
            for chamado in self.__listaChamados:
                if (chamado.data == data) and (chamado.cliente == cliente) and (chamado.tecnico == tecnico) and (chamado.tipo == tipo):
                    print("Chamado já existente")
                else:
                    novoChamado = Chamado(data, cliente, tecnico, titulo,
                                        descricao, prioridade, tipo)
                    self.__listaChamados.append(novoChamado)

                    return novoChamado

    def incluiTipoChamado(self, codigo: int, nome: str, descricao: str) -> TipoChamado:
        if self.__tipoChamados == []:
            novo_tipo = TipoChamado(codigo, descricao, nome)
            self.__tipoChamados.append(novo_tipo)
            return novo_tipo
        else:
            for tipo in self.__tipoChamados:
                if tipo.codigo == codigo:
                    print("Tipo já cadastrado")
                else:
                    novo_tipo = TipoChamado(codigo, descricao, nome)
                    self.__tipoChamados.append(novo_tipo)
                    return novo_tipo
