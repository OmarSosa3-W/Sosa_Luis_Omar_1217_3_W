print(" ")#para dejar un espacio
print("SOSA LUIS OMAR 3-W: MI PRACTICA DE NUMEROS TRIUNFADORES")#nomrbe del creador 
print(" ")#para dejar un espacio
#el bucle (for) para comenzar la lista de 6 numeros
numeros_triunfadores = [int(input("Ingresa un número triunfador: ")) for _ in range(6)]#pide al usuario que ingrese un numero 

numeros_triunfadores.sort()#se coloca la condicion a imprimir

print("Los números triunfadores en orden son:", numeros_triunfadores)#muestra el resultado en pantalla
print(" ")#para dejar un espacio