from db import nova_conexao
from mysql.connector.errors import ProgrammingError

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM contatos LIMIT 5 OFFSET 8')
        contatos = cursor.fetchall()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        [print(f'{contato[2]:2d} - {contato[0]:6s} Telefone: {contato[1]}')
         for contato in contatos]
