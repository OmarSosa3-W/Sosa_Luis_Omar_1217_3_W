# Sosa_Luis_Omar_1217_3_W
Envío de la primera practica de la unidad 2

1 PROGRAMA DE LAS METERIAS ALMACENADAS EN UN CURSO
# Crear una lista de materias
print(" ")#se coloca la para dejar un espacio al ejecutar
print("SOSA LUIS OMAR 3-W: MI PRACTICA DE MATERIAS")#nombre del creador del codigo
print(" ")#se coloca la para dejar un espacio al ejecutar
materias = ["Pensamiento matemático", "Español", "Inglés", "Química", "Civismo", "Francés"]#declarando variables 

# Desplegar la lista en pantalla
for materia in materias:#se coloca la condicion a imprimir
    print(materia)#se imprime la condicion 
    # Desplegar el mensaje personalizado para cada materia
    print(" ")#se coloca la para dejar un espacio al ejecutar
for materia in materias:
    print(" ")#se coloca la para dejar un espacio al ejecutar
    print(f"Estoy cursando {materia}")#el resultado en pantalla 
    print(" ")#se coloca la para dejar un espacio al ejecutar
    calificaciones = []#muetsralas en pantalla 

for materia in materias:#se coloca la condicion a imprimir
    calificacion = input(f"Ingresa tu calificación para {materia}: ")#se imprime el resultado 
    calificaciones.append(calificacion) #muestra el resultado en pantalla 

# Desplegar las calificaciones correspondientes
for materia, calificacion in zip(materias, calificaciones):
    print(" ")#se coloca la para dejar un espacio al ejecutar
    print(f"En {materia} has obtenido {calificacion}.")#muetsra las calificaciones 

![image](https://github.com/user-attachments/assets/5fe5a170-f046-4b6e-b3dc-440de509a8a4)


![image](https://github.com/user-attachments/assets/443fedb7-53fd-481a-bf22-2fc20fe27091)
