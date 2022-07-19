from time import sleep


def contador(inicio, fim, passo):
    if passo < 0:
        passo = passo * -1
    if passo == 0:
        passo = 1
    print(f'Contando de {inicio} até {fim} , pulando {passo}')
    if inicio<fim:
        for c in range(inicio, fim+1, passo):
            print(c, end=' ')
            sleep(1)
        print('FIM!')
        print('=-'*30)
    sleep(1)
    if inicio>fim:
        for c in range(inicio,fim-1, -passo):
            print(c, end=' ')
            sleep(1)
        print('FIM!')
        print('=-' * 30)


contador(1,10,1)
contador(10,0,2)
print('Agora é a sua vez de personalizar a contagem!!')
ini = int(input('Início: '))
fi= int(input('Fim: '))
pa = int(input('Passo: '))
contador(ini,fi,pa)
