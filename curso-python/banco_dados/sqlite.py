from sqlite3 import connect, ProgrammingError, Row

tabela_contatos = """
    CREATE TABLE IF NOT EXISTS contatos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(50),
        tel VARCHAR(40),
        grupo_id INTEGER,
        FOREIGN KEY (grupo_id) REFERENCES grupos(id)
    )
"""

tabela_grupos = """ 
    CREATE TABLE IF NOT EXISTS grupos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        descricao VARCHAR(30)
    )
"""

insert_grupo = 'INSERT INTO grupos (descricao) VALUES (?)'
select_grupos = 'SELECT id, descricao FROM grupos'
insert_contatos = 'INSERT INTO contatos (nome, tel, grupo_id) VALUES (?, ?, ?)'
select = """
    SELECT
        g.descricao AS grupo,
        c.nome AS contato
    FROM contatos c
    INNER JOIN grupos g
    ON g.id = c.grupo_id
    ORDER BY grupo, contato
"""

try:
    conexao = connect(':memory:')
    conexao.row_factory = Row

    cursor = conexao.cursor()
    cursor.execute(tabela_grupos)
    cursor.execute(tabela_contatos)

    cursor.executemany(insert_grupo, (('casa', ), ('trabalho',)))
    cursor.execute(select_grupos)
    grupos = {row['descricao']: row['id'] for row in cursor.fetchall()}
    print(grupos)

    contatos = {
        ('Arthur', '456', grupos['casa']),
        ('Paulo', '789', grupos['casa']),
        ('Angelo', '000', grupos['trabalho']),
        ('Eduardo', '987', None),
        ('Yuri', '654', None),
        ('Leonardo', '321', None),
    }
    cursor.executemany(insert_contatos, contatos)

    cursor.execute(select)
    for contato in cursor:
        print(contato['contato'], contato['grupo'])
except ProgrammingError as e:
    print(f'Erro: {e.msg}')
