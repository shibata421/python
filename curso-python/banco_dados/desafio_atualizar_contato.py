from db import nova_conexao
from mysql.connector.errors import ProgrammingError

sql = """
    UPDATE contatos
    SET nome = %s
    WHERE id = %s
"""

args = ('Shie', 6)

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql, args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro {e.msg}')
    else:
        print(f'{cursor.rowcount} registro(s) atualizados')
