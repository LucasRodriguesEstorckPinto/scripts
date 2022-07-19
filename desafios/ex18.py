print('calculo de seno, cosseno e tangente de um ângulo')
from math import sin,cos,tan, radians
n = float(input('Digite aqui um ângulo:'))

print(f'O seno do ângulo {n} é {sin(radians(n)):.2f}\nO cosseno é {cos(radians(n)):.2f}\nA tangente é {tan(radians(n)):.2f}')

