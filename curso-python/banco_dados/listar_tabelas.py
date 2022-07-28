from mysql.connector.errors import ProgrammingError
from db import nova_conexao

listar_tabelas_sql = """
    SHOW TABLES
"""

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(listar_tabelas_sql)
        for i, tabelas in enumerate(cursor, start=1):
            print(f'{i} - {tabelas[0]}')
    except ProgrammingError as e:
        print(f'erro: {e.msg}')
