"""
Práctica 02: Calcular Precio de Venta

Enunciado: dado el valor de venta de productos, 
hallar el igv(18%) y el precio de venta.
Análisis: para la solucion de este problema,
se requiere que el usuario ingrese el valor de venta del producto
y el sistema realice el cálculo respectivo para hallar
el igv y el precio de venta, para esto use la siguiente
exprecion.

igv = vv * 0.18

pv = vv + igv
"""
#ingreso de datos
vv=input("Digite valor de venta: ")
vv=float(vv)
igv=0.18
#Operaciones
igv = float (igv)
igv = vv * 0.18
pv = vv + igv
#Resultado

print ("El precio es: ",pv)
print ("El IGV es: ",igv)





