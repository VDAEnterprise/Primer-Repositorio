print("Convertidor de Segundos")
#Ingreso de Datos
T = int(input("Ingresa los Segundos: "))
#Operacion
H = T * (1.0 / 3600.0)
M = T * (1.0 / 60.0)
S = M * (60.0 / 1.0)
#Resultado
print("Las Horas Son: ", H)
print("Los Minutos Son: ", M)
print("Los Segundos Son: ", S)



