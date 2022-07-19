from random import randint
numeros = []
so = []


def sorteia():
    for c in range(0,5):
        numeros.append(randint(1,20))


def somapar():
    s = 0
    for c in numeros:
        if c%2==1:
            numeros.remove(c)
            s = sum(numeros)
    so.append(s)


sorteia()
print(f'Os números sorteados foram {numeros}')
somapar()
print(f'A soma dos números pares {numeros} é igual a {so[0]}')