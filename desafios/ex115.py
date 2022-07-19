
def tabuada(n):
    for c in range(1,11):
        print(f'{c:^2} x {n} = {n*c:>2}')


h = int(input('número para ver a tabuada: '))
tabuada(h)
