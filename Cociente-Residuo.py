"""
Practica 01: Calcular cociente y residuo
Enunciado: hallar el cociente y el residuo
(resto) de dos números enteros.
Análisis: para la solución de este problema,
se requiere que el usuario ingrese dos números
enteros y el sistema realice el cálculo respectivo 
para hallar el cociente y residuo.
"""
print ("Calculo de Cociente y Residuo")
#Ingreso de datos
a = input("digite primer numero: ")
b = input("digite segundo numero: ")

#operacion
a = int(a)
b = int(b)
cociente = (a // b)#para arrojar solo el coceinte (//)
residuo = (a % b)#para arrojar solo el residuo (%)

print("el cociente es: ", cociente)
print("el residuo es: ", residuo)




