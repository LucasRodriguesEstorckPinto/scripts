soma = 0
n = 0
for c in range(1, 501):
    if c % 2 == 1 and c % 3 == 0:
        n = n + 1
        soma = soma + c
print(f'A soma dos {n} números é {soma}')
