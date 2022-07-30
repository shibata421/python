from db import nova_conexao
from mysql.connector.errors import ProgrammingError

sql = """
    DELETE FROM contatos WHERE nome = %s
"""

nome = ('Lucas', )

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql, nome)
        conexao.commit()
    except ProgrammingError as e:
        print(f'erro: {e.msg}')
    else:
        print(f'{cursor.rowcount} registro(s) deletados')