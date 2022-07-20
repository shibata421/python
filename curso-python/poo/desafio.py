#!/usr/bin/python3
from datetime import datetime, timedelta
from pessoa import Vendedor, Cliente
from compra import Compra

if __name__ == "__main__":
    vendedor = Vendedor('Fernando', 31, 3000)
    print(vendedor)

    cliente = Cliente('Cinthia', 31)
    compra1 = Compra(vendedor, datetime.now() - timedelta(days=1), 3000)
    compra2 = Compra(vendedor, datetime.now() - timedelta(days=25), 5000)
    compra3 = Compra(vendedor, datetime.now() - timedelta(weeks=5), 9000)
    cliente.registrar_compras(compra1, compra2, compra3)

    print(cliente.get_data_ultima_compra())
    print(cliente.is_adulto())
    print(cliente.total_compras())
