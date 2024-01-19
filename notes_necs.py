c1 = int(input("Ingrese la nota del certamen 1: "))
c2 = int(input("Ingrese la nota del certamen 2: "))
note_lab = int(input("Ingrese la nota del laboratorio: "))

c3 = ((60 - note_lab * 0.3) / 0.7 ) * 3 - c1 - c2

print(f"Necesita {round(c3)} en el certamen 3 para pasar el ramo con una nota final de 60")
