#CREAR UN PROGRAMA QUE PERMITA INGRESAR LOS NUMEROS DE N ALUMNOS
nAlumnos = int(input("INGRESE LA CANTIDAD DE ALUMNOS: "))
iterador = 1
while nAlumnos >= iterador:
    nombre = input("INGRESE EL NOMBRE DEL ALUMNO {}:".format(iterador))
    iterador += 1