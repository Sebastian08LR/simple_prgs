import math 
def horario_futuro(hora, h):
    total_horas = h
    horas_actuales = hora
    horas_futuras = (horas_actuales + total_horas) % 24
    return horas_futuras


hora_actual = float(input("Ingrese la hora actual con minutos(separados por un punto): "))  #  print ("ingresa una hora menor a 24: \n")

h = float(input("Cuantas horas quiere sumar: "))

hora_futura = horario_futuro(hora_actual, h)
parte_decimal, parte_entero = math.modf(hora_futura)
if parte_decimal*100 >60:
    print("\n\t----Recuerde que los minutos van hasta 60-----")
else:
    print(f"Dentro de {h} horas, serán las {int(parte_entero)}:{int(parte_decimal*100)}")
    