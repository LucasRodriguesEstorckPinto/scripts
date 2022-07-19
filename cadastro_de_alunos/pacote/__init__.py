def tit(msg):
    lin = 42 
    print('~'*lin)
    print(msg.center(42))
    print('~'*lin)


def num(n):
    while True:
        try:
            num = int(input(n))
        except:
            print('\033[31mAPENAS NUMEROS INTEIROS\033[m')
        else:
            return num 


def verifica(arqui):
    try:
        a = open(arqui,'rt')
        a.close()
    except FileNotFoundError:
        print()
    else:
        return True

def cria(arqui):
    try:
        a = open(arqui,'wt+')
        a.close()
    except:
        print('ERRO INESPERADO')
    else:
        print(f'{arqui} criado')


def escreve(arqui,lista):
    a = open(arqui,'a')
    a.write(f'Nome = {lista[0]:<5} || 1° nota = {lista[1]:<5} 2° nota ={lista[2]:<5} média = {lista[3]}\n')
    a.close()



def escolha(lista):
    for c in range(0,len(lista)):
        print(f'\033[35m{c+1:<4}\033[m-\033[36m{lista[c]}\033[m')


def sn(a):
    while True:
        res = str(input(a)).strip().upper()[0]
        if res == 'N':
            return 'N'
        elif res =='S':
            return 'S'
        else:
            print('\033[31mAPENAS SIM OU NÃO\033[m')

def ler(arqui):
    a = open(arqui,'rt')
    print(a.read())
    a.close()