from db import nova_conexao
from mysql.connector.errors import ProgrammingError

sql = """
    INSERT INTO contatos (nome, tel)
    VALUES (%s, %s)
"""

args = (
    ('Ana', '98765-4321'),
    ('Bia', '88765-4321'),
    ('Luca', '78765-4321'),
    ('Lu', '68765-4321'),
    ('Gui', '58765-4321'),
    ('Beca', '48765-4321'),
    ('Pedro', '38765-4321'),
    )

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.executemany(sql, args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print(f'Foram incluídos {cursor.rowcount} registros')