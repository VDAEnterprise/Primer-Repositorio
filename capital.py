print("Interes Compuesto")
#ingrese datos
c = int(input("Ingrese Capital: "))
r = float(input("Ingrese la Tasa Interes: "))
t = int(input("Ingrese Lapso de Tiempo: "))
#Operacion
m = pow(1+r/100,t)*c
i = m - c
#resultado
print("El monto es: ",m)
print("El Interes es: ",i)

