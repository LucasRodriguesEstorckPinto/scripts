print('=-' * 20)
print(f'{"Analisador de números":^40}')
print('=-' * 20)
l = []
for c in range(0, 5):
    l.append(int(input(f'Digite o {c} número: ')))
    print('_' * 20)
print('=-' * 20)
print(f'O maior número é o {max(l)} e ele está nas posições ', end='')
for c in range(0, len(l)):
    if l[c] == max(l):
        print(f'{c}...', end='')
print(f'\nE o menor é o {min(l)}, estando nas posições ', end='')
for c in range(0, len(l)):
    if l[c] == min(l):
        print(f'{c}...', end='')
