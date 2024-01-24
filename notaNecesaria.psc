Algoritmo notaNecesaria
	Definir c1 Como Entero
	Definir c2 Como Entero
	Definir noteLab Como Entero
	Definir c3 Como Real
	Escribir "Ingrese la nota de c1: "
	Leer c1
	Escribir "Ingrese la nota de c2: "
	Leer c2
	Escribir "Ingrese la nota del Laboratorio: "
	Leer noteLab
	
	c3 = trunc(((60 - noteLab * 0.3) / 0.7 ) * 3 - c1 - c2)
	
	Escribir "La nota que necesita en el c3 es: ", c3
FinAlgoritmo
