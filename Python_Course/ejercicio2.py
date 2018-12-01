#! /user/bin/python
# -*- coding: iso-8859-15
from random import *
n = int(input("Ingrese la cantidad de tiros: "))
x = 0
for i in range(n):
    x = randint(1 ,6)
    print(x)
    if x == 3:
        break
print("El lanzamiento en el que salio el 3 fue: " ,i+1)
