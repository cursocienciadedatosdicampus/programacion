'''
Crear un programa, que dibuje un triángulo de asteriscos, cuyo número de lado de asteriscos,
tantos como el número introducido por teclado
'''

x=int(input("Introduce la dimension del triangulo:"))
for i in range(0,x):  # le va a indicar el número de lineas
    for i in range(0,i+1):   # para cada linea recorre la cantidad de asteriscos que va a imprimir
        print('*',end=" ")   # imprime un asterisco 
    print()  # imprime el salto de linea, tras cada linea de asteriscos
