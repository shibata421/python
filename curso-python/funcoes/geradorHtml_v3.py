def tag_bloco(conteudo, classe='success', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}">{conteudo}</{tag}>'


def tag_lista(*itens):
    lista = ''.join(f"<li>{item}</li>" for item in itens)
    return f"<ul>{lista}</ul>"


if __name__ == '__main__':
    lista_nomes = tag_lista('ana', 'bia', 'carlos')
    print(tag_bloco(lista_nomes, classe="info"))
