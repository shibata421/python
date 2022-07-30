from db import nova_conexao

sql = """
    SELECT tel, nome 
    FROM contatos
    WHERE nome LIKE 'Lu%'
"""

with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute(sql)
    
    for x in cursor:
        print(x)
