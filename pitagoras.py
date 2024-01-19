import math

catetoA = float(input("Ingrese el valor del cateto A: "))
catetoB = float(input("Ingrese el valor del cateto B: "))

catetoC = math.sqrt((math.pow(catetoA,2) + math.pow(catetoB,2))) # or **0.5 sin utilizar math
print(f"La hipotenusa es: {catetoC}")
