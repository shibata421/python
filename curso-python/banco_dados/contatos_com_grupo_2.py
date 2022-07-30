from db import nova_conexao
from mysql.connector.errors import ProgrammingError
from collections import defaultdict

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
        try:
            cursor.execute(sql)
            contatos = cursor.fetchall()
        finally:
            cursor.close()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        agrupados = defaultdict(list)
        for contato in contatos:
            agrupados[contato['grupo']].append(contato['contato'])
        
        print(agrupados)
