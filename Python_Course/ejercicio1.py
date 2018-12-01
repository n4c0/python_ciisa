#! /user/bin/python
# -*- coding: iso-8859-15
n = int(input('Cantidad de Caucho: '))
p = float(1000)
if n >= 6:
    print ('Aplica Descuento 15%')
    sub=n*p
    des=sub*0.15
    total=sub-des
else:
    print  ('No aplica Descuento 10%')
    sub=n*p
    des=sub*0.10
    total=sub-des
print("El total de cauchos: " ,n)
print("El precio total es: " ,p)
print("El descuento es: " ,des)
print("El total a pagar: " ,total)
