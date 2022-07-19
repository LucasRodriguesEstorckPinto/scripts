def leiaInt(n):
    while True:
        try:
            j = int(input(n))
        except KeyboardInterrupt:
            print('\n\033[31mO usuário preferiu não digitar nada.\033[m')
            return 0
        except Exception as erro:
            print('\033[31mERRO: DIGITE UM NÚMERO INTEIRO VÁLIDO\033[m')
            continue
        else:
            return j


def leiafloat(n):
    while True:
        try:
            j = float(input(n))
        except KeyboardInterrupt:
            print('\n\033[31mO usuário preferiu não digitar nada\033[m')
            return 0
        except Exception as erro:
            print('\033[31mERRO: DIGITE UM NÚMERO REAL VÁLIDO\033[m')
        else:
            break
    return j


i = leiaInt('Digte um número inteiro: ')
r = leiafloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {i} e o real foi {r}')