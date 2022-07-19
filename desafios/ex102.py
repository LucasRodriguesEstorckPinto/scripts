def fatorial(a, show=False):
    """
    Calcula o fatorial de um número
    :param a: O número a ser calculado
    :param show: (opcional) Mostra ou não a conta
    :return: O valor do fatorial de um número n.
    """
    f = 1
    if show:
        print('__' * 20)
        for c in range(a, 0, -1):
            f = f * c
            if c>1:
                print(f'{c} x ',end=' ')
            if c==1:
                print(f'{c} = {f}')
        return f
    elif not show:
        for c in range(a, 0, -1):
            f = f * c
        print('__' * 20)
        print(f'{f}')
    return f


fatorial(6,show=True)
