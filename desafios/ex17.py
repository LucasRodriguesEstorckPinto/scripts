import math
print('Calculadora de hipotenusa')
co = float(input("DIGITE AQUI O CATETO OPOSTO:"))
ca = float(input("DIGITE AQUI O CATETO ADJACENTE:"))

print(f"A HIPOTENUSA É:{math.hypot(co , ca):.2f}")

