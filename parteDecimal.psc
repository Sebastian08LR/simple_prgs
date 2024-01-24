Algoritmo parteDecimal
	Definir num1 Como Real
    Definir res Como Real
	Escribir "Ingrese un numero: "
	Leer num1 
	res = ( num1 - trunc(num1)) * 100
	Escribir "La parte decimal del numero que ingresó es: ", res
FinAlgoritmo
