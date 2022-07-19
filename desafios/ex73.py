c = (
'Palmeiras', 'Atlético-MG', 'Fortaleza', 'Bragantino', 'Athletico-PR', 'Ceará', 'Bahia', 'Fluminense', 'Atlético-GO',
'Flamengo', 'Santos', 'Corinthians', 'Juventude', 'São Paulo', 'Internacional', 'Amériga-MG', 'Cuiabá', 'Sport',
'Grêmio', 'Chapecoense')

for h in range(0, 5):
    print(f'O {h + 1}° colocado é: {c[h]}')
print('=-' * 20)

for h in range(16, 20):
    print(f'O {h + 1}° colocado é {c[h]}')
print('=-' * 20)
print(f'Os times em ordem alfabética fica assim:')
for h in sorted(c):
    print(h,end='\n')
print('=-' * 20,end='\n')

for pos, time in enumerate(c):
    if time == 'Chapecoense':
        print(f'O time {time} está em {pos + 1}°')
