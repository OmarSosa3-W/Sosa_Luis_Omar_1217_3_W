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

2 PROGRAMA DE PRECIOS MENOY/MAYOR
#pide al usuario que almacene precios y diga cual es mayor y cual es menor
print(" ")#se coloca para dejar un espacio al ejecutar
print("SOSA LUIS OMAR 3-W: MI PRACTICA DE NUMEOS MAYOR O MENOR")#nombre del creador del programa
print(" ")#se coloca para dejar un espacio al ejecutar
precios = [43, 57, 92, 20, 37, 5, 9]#definir las variables/numeros

precio_mayor = max(precios)#Calcular el precio mayor y el precio menor
precio_menor = min(precios)#Calcular el precio mayor y el precio menor

print("Precio mayor:", precio_mayor)# Mostrar los resultados
print(" ")#se coloca para dejar un espacio al ejecutar
print("Precio menor:", precio_menor)# Mostrar los resultados
print(" ")#se coloca para dejar un espacio al ejecutar

![image](https://github.com/user-attachments/assets/1e595ffb-880d-4e49-86cd-a76120255990)

![image](https://github.com/user-attachments/assets/ef53cf05-df00-4b65-8a4d-74ea2cff27ce)

3 PROGRAMA DE NUMEROS GANADORES 
print(" ")#para dejar un espacio
print("SOSA LUIS OMAR 3-W: MI PRACTICA DE NUMEROS TRIUNFADORES")#nomrbe del creador 
print(" ")#para dejar un espacio
#el bucle (for) para comenzar la lista de 6 numeros
numeros_triunfadores = [int(input("Ingresa un número triunfador: ")) for _ in range(6)]#pide al usuario que ingrese un numero 

numeros_triunfadores.sort()#se coloca la condicion a imprimir

print("Los números triunfadores en orden son:", numeros_triunfadores)#muestra el resultado en pantalla
print(" ")#para dejar un espacio

![image](https://github.com/user-attachments/assets/64d16bb4-486d-4b71-a814-9e51474be6f2)
![image](https://github.com/user-attachments/assets/b05cc2dc-367b-49a6-a57c-2f832596da08)


