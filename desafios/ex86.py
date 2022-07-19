linha1 = [[], [], []]
linha2 = [[], [], []]
linha3 = [[], [], []]
for c in range(0,3):
    linha1[c].append(int(input(f'Digite um valor para [0,{c}]:')))
for c in range(0,3):
    linha2[c].append(int(input(f'Digite um valor para [1,{c}]:')))
for c in range(0,3):
    linha3[c].append(int(input(f'Digite um valor para [2,{c}]:')))
print('==='*20)
for n in linha1:
    print(f'{n}', end='   ')
print()
for n1 in linha2:
    print(n1,end='   ')
print()
for n2 in linha3:
    print(n2,end='   ')
print()
print('==='*20)
