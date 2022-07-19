c = s= 0
while True:
    n = int(input(f'Digite o {c+1}° número: '))
    if n==999:
        break
    c = c + 1
    s = s + n
print(f'A soma de todos os {c} números mostrados é {s}.')