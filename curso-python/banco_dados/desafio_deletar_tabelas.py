from db import nova_conexao
from mysql.connector.errors import ProgrammingError

deletar_tabela_sql = """
    DROP TABLE IF EXISTS emails
"""

try:
    with nova_conexao() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(deletar_tabela_sql)
        except ProgrammingError as e:
            print(f'erro: {e.msg}')
except ProgrammingError as e:
    print(f'erro: {e.msg}')
