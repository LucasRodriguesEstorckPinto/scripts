a = input('DIGITE UMA FRASE QUALQUER:').strip().upper()
qa = a.count('A')
print(f'a letra A aparece {qa} vezes')
pos = a.find('A')+1
print(f'Ela aparece pela primeira vez em {pos}')
ult = a.replace(' ','').rfind('A')+1
print(f'Ela aparece pela ultima vez em {ult}')
