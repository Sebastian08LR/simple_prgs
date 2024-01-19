notes = list([])
cant_notes = int(input("Ingrese la cantidad de notas que guardará: "))
sum_notas = 0
for nota in range(cant_notes):
    average = sum_notas/cant_notes
    notas = notes.append(float(input(f"Ingrese la nota numero {nota+1}: ")))
    sum_notas += notas

print(f"\n\n\tEl promedio de las notas es {average}")
        