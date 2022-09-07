# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 14:25:13 2022

@author: datos
"""
'''
Función que recibe una matriz como parámetro y la imprime por pantalla
'''
def mostrarmatriz(matriz):
    for i in range(0,len(matriz)):
        for j in range(0,len(matriz[i])):
            print(matriz[i][j],end=" ")
        print()

dimension=int(input("Introduce una dimension="))
matriz=[]
for i in range(0,dimension):
    lista=[]
    for j in range(0,dimension):
        lista.append(0)
    matriz.append(lista)
    
mostrarmatriz(matriz)

recorrido=0
if (dimension%2==0):
    recorrido=round(dimension/2)
else:
    recorrido=dimension//2+1

for i in range(0,recorrido):
    print("*****************************")

    print(i)
    for j in range(i,dimension-i):
        matriz[i][j]=i+1
        matriz[dimension-i-1][dimension-j-1]=i+1
    #print(matriz[i])
    for k in range(i,dimension-i):
        matriz[k][i]=i+1
        matriz[dimension-k-1][dimension-i-1]=i+1
    mostrarmatriz(matriz)
print("*****************************")

mostrarmatriz(matriz)