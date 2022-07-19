total = [[], []]
for c in range(1,8):
    n = int(input(f'Digite o {c}° valor: '))
    if n%2==0:
        total[0].append(n)
    else:
        total[1].append(n)
total[0].sort()
total[1].sort()
print('==='*20)
print(f'Os valores pares digitados foram: {total[0]}')
print(f'os valores ímpares digitados foram: {total[1]}')
