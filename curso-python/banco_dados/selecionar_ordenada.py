from db import nova_conexao

sql = """
    SELECT nome 
    FROM contatos
    ORDER BY nome DESC
"""

with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute(sql)
    
    print('\n'.join(campo[0] for campo in cursor))
