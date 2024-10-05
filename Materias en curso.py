print(" ")#se coloca para dejar un espacio
print("SOSA LUIS OMAR 3-W: MI PRACTICA DE METERIAS ")#nombre del creador
print(" ")#se coloca para dejar un espacio

materias = ["Pensamiento matemático", "español", "Inglés", "química", "civismo", "francés"]#se declaran variables 

# Recorrer la lista de materias y mostrar un mensaje para cada una
for materia in materias:#se coloca la condicion a imprmir
    print(" ")#se coloca para dejar un espacio
    print(f"Estoy cursando {materia}")#mustra el cursamiento de cada materia 
    materias = ["Pensamiento matemático", "español", "Inglés", "química", "civismo", "francés"]#colocan las variables a cursar

# Diccionario para almacenar las calificaciones
calificaciones = {}#se coloca para la condicion 

# Solicitar la calificación para cada materia
for materia in materias:#se coloca la condicion a imprmir
    calificacion = input(f"Introduce tu calificación en {materia}: ")#pide ingresar una calificacion 
    print(" ")#se coloca para dejar un espacio
    calificaciones[materia] = calificacion#muestra el resultado en pantalla 

# Mostrar las calificaciones para todas las materias
print("\nTus calificaciones:")#la variable a imprimir
for materia, calificacion in calificaciones.items():#se coloca para mostrar todo en pantalla 
    print(f"En {materia} has obtenido {calificacion}")#el resultado final