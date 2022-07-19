print('--Calculador de empréstimos--')
a = float(input('Digite o valor do imóvel: '))
b = float(input('Digite seu salário: '))
c = int(input('Em quantos anos deseja pagar o empréstimo?: '))
prest = (a/(12*c))

if prest <= (30/100)*b:
    print(f'A prestação mensal será de R${prest:.2f}')
    print('Empréstimo aceito')
else:
    print(f'\033[31mEmpréstimo negado\033[m, você não pode pagar mensalmente a prestação de R$ {prest:.2f} ao mês ')
