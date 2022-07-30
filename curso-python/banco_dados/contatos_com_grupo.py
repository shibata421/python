from db import nova_conexao
from mysql.connector.errors import ProgrammingError

sql = """
    SELECT 
        g.descricao AS grupo,
        c.nome AS contato
    FROM contatos c
    INNER JOIN grupos g
    ON c.grupo_id = g.id
    ORDER BY grupo, contato
"""

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor(dictionary=True)
        cursor.execute(sql)
        for campos in cursor:
            print(' : '.join((campos['grupo'], campos['contato'])))
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')

