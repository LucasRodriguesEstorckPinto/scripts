sim = []
n = str(input('Digite uma expressão: '))
for s in n:
    if s=='(':
        sim.append(s)
    elif s==')':
        if len(sim)>0:
            sim.pop()
        else:
            sim.append(')')
            break
if len(sim)==0:
    print('Expressão válida')
else:
    print('Expressão inválida')