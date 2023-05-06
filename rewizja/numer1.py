def suma_iter(liczby):
    suma = 0
    for x in liczby:
        suma += x
    return suma
print(suma_iter([2, 3, 5]))

def suma_rec(liczby):
    if len(liczby) == 0:
        return 0
    return liczby[0] + suma_rec(liczby[1:])
print(suma_rec([2, 3, 5]))

def iloczyn_iter(liczby):
    iloczyn = 1
    for x in liczby:
        iloczyn *= x
    return iloczyn
print(iloczyn_iter([2, 3, 5]))

def iloczyn_rec(liczby):
    if len(liczby) == 0 : return 1
    return liczby[0] * iloczyn_rec(liczby[1:])
print(iloczyn_rec([2, 3, 5]))

import math
def minimum_iter(liczby):
    minimum = math.inf
    for x in liczby:
        if x< minimum:
            minimum = x
    return minimum
print(minimum_iter([2, 3, 5]))

def minimum_rec(liczby):
    if len(liczby) == 0:
        return math.inf
    minimogona = minimum_rec(liczby[1:])
    if liczby[0] < minimogona:
        return liczby[0]
    return minimogona
print(minimum_rec([2, 3, 5]))

def silnia_iter(liczba):
    silnia = 1
    for x in range(1, liczba+1):
        silnia *= x
    return silnia
print(silnia_iter(3))

def silnia_rec(n):
    if n == 0 : return 1
    return n * silnia_rec(n-1)
print(silnia_rec(3))

def fibb(n):
    if n == 0: return 0
    if n == 1: return 1
    return fibb(n-1) + fibb(n-2)
print([fibb(x) for x in range(10)])

def kwadraty_iter(liczby):
    kwadraty = []
    for x in liczby:
        kwadraty.append(x**2)
    return kwadraty
print(kwadraty_iter([1, 2, 3, 4, 5]))


def kwadraty(liczby):
    if len(liczby) ==0: return []
    return [(liczby[0])**2] + kwadraty(liczby[1:])

print(kwadraty([1, 2, 3, 4, 5]))

