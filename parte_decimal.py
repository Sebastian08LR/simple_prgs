import math
num = float(input("Ingrese un numero con decimales(Utilice '.' no ','): "))

#separa el numero en dos variables, una parte agarra el valor decimal del numero  la otra la parte entera
parte_decimal, parte_entera = math.modf(num)

print(f"Del numero {num}, la parte decimal es: {parte_decimal}")

