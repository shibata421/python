from db import nova_conexao

selecionar_grupo = 'SELECT id FROM grupos WHERE descricao = %s'
atualizar_contato = 'UPDATE contatos SET grupo_id = %s WHERE nome = %s'

contato_grupo = {
    'Shie' : 'casa',
    'Bia' : 'trabalho',
    'Luca' : 'trabalho',
    'Lu' : 'trabalho',
    'Gui' : 'casa',
    'Beca' : 'trabalho',
    'Pedro' : 'casa',
    'Ana' : 'casa',
}

with nova_conexao() as conexao:
    cursor = conexao.cursor()
    for contato, grupo in contato_grupo.items():
        cursor.execute(selecionar_grupo, (grupo, ))
        id = cursor.fetchone()[0]
        cursor.execute(atualizar_contato, (id, contato))
        conexao.commit()