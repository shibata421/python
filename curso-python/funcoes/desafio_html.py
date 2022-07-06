#!/usr/bin/python3
def htmlTag(function):
    def decorator(*args, **kwargs):
        if 'css' in kwargs:
            kwargs['class'] = kwargs.pop('css')

        atributos = ' '.join(f'{key}="{value}"' for key, value in kwargs.items())

        conteudo = function(*args, **kwargs)

        return f'<{args[0]} {atributos}>{conteudo}</{args[0]}>'

    return decorator


@htmlTag
def tag(tag, *args, **kwargs):
    return ''.join(args)


if __name__ == '__main__':
    # print(tag('span', 'Curso de Python 3, por '))
    
    # print(tag('p', tag('span', 'Curso de Python 3, por ')))
    
    print(
        tag('p',
            tag('span', 'Curso de Python 3, por '),
            tag('stong', 'Juracy Filho', id='jf'),
            tag('span', ' e '),
            tag('strong', 'Leonardo Leitão', id='ll'),
            tag('span', '.'),
            css='alert')
    )

    # <p class="alert">
    #   <span >Curso de Python 3, por </span>
    #   <strong id="jf">Juracy Filho</strong>
    #   <span > e </span>
    #   <strong id="ll">Leonardo Leitão</strong>
    #   <span >.</span>
    # </p>