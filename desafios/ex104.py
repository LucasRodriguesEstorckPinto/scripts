def leiaint(nu):
    global n
    while True:
        n = input(nu)
        if not n.isnumeric():
            print('\033[1;31mERRO! Digite um número inteiro válido\033[m')
        if n.isnumeric():
            break
    return n


n = leiaint('Digite um número: ')
print(f'Você digitou o número {n}')