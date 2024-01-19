import math
TH = float(input("Temperatura inicial del huevo: "))
TE = 100
M = 47
densidad = 1.038
C = 3.7
K = 0.0054

dividendo = (math.pow(M, (2/3)) * ( C * math.pow(densidad,(1/3))))

divisor = (K * math.pow(math.pi, 2)) * math.pow((4*math.pi) / 3, (2/3))
resultado = dividendo/divisor
resultado2 = math.log(0.76 * ((TH - TE) / (70 - TE)))
segundos = resultado * resultado2
minutos = round(segundos/60)

print(f"El tiempo máximo para prepararlo a la copa {round(segundos)} seg")
print(f"El tiempo máximo para prepararlo a la copa {minutos} min")