rad = float(input("Ingrese el radio del circulo: "))

def cirulo_calc(radio):
    #PROCESOS
    pi = 3.1416
    area = pi*radio**2
    perimetro = 2*pi*radio
    #OUTPUTS
    print(f"El area del circulo con radio {radio} es {area}")
    print(f"El perimetro del circulo con radio {radio} es {perimetro}")

cirulo_calc(rad)
    
