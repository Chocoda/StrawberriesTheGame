def fibb (n):
    if n == 0 : return 0
    if n == 1 : return 1
    return fibb(n-1) + fibb(n-2)

def silnia(n):
    if n == 0: return 1
    return n * silnia(n-1)
print(silnia(5))

def suma(lista):
    suma = 0
    for x in lista:
        suma += x
    return suma
print(suma([1, 2, 5]))

def suma_rec(list):
    if len(list) == 0: return 0
    return list[0] + suma_rec(list[1:])
print(suma_rec([1, 2, 5]))

import math
def minimum(liczby):
    minim = math.inf
    for x in liczby:
        if x < minim:
            minim = x
    return minim

print(minimum([1, 2, 5]))


