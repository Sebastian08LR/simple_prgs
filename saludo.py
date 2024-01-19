nom = input("Ingrese su nombre: ")
sex = input("\nIngrese su sexo: ")

def saludo(nombre,sexo):
    sexo  = sexo.lower()
    if sexo == "mujer":
        print(f"Hola bunos días sra {nombre}")
    elif sexo == "hombre":
        print(f"Hola buenos días sr {nombre}")
        
    
saludo(nom,sex)