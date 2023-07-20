#CREAR UN PROGRAMA QUE PERMITA INGRESAR LOS NOMBRES DE N ALUMNOS Y LA CANTIDAD M DE CURSOS
N = int(input("Ingrese la cantidad de estudiantes: "))
i = 1

while N >= i:
    nombre = input("Alumno {}: ".format(i))
    M = int(input("Ingrese la cantidad de cursos: ")) 
    j = 1
    while M >= j:
        curso_nombre = input("Curso {}: ".format(j) )
        j+=1

    i += 1
