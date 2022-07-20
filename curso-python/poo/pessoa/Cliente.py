from .Pessoa import Pessoa


class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.compras = []

    def registrar_compras(self, *compras):
        [self.compras.append(compra) for compra in compras]

    def get_data_ultima_compra(self):
        return sorted(self.compras, key=lambda compra: compra.data)[-1].data

    def total_compras(self):
        total = 0
        for compra in self.compras:
            total += compra.valor

        return total
