def suma_iter(liczby):
    suma = 0
    for x in liczby:
        suma += x
    return suma
print(suma_iter([3, 4, 5]))

def suma_rec(liczby):
    if len(liczby) == 0: return 0
    return liczby[0] + suma_rec(liczby[1:])
print(suma_rec([3, 4, 5]))

import math
def minim_iter(liczby):
    minimum = math.inf
    for x in liczby:
        if x< minimum:
            minimum = x
    return minimum
print(minim_iter([3, 4, 5]))

import math
def minim_rec (liczby):
    if len(liczby) == 0: return math.inf
    minimum_z_ogona = minim_rec(liczby[1:])
    for x in liczby:
        if liczby[0] < minimum_z_ogona:
            return liczby[0]
        return minimum_z_ogona
print(minim_rec([3, 4, 5]))

def silnia_iter(n):
    silnia = 1
    for x in range (1,n+1):
        silnia *= x
    return silnia
print(silnia_iter(5))

def silnia_rec(n):
    if n ==0 : return 1
    return n * silnia_rec(n-1)
print(silnia_rec(5))

def fib (n):
    if n == 0: return 0
    if n == 1: return 1
    return fib(n-1) + fib(n-2)
print([fib(x) for x in range(10)])

def kwadraty_iter (liczby):
    kwadraty = []
    for x in liczby:
        kwadraty.append(x**2)
    return kwadraty
print(kwadraty_iter([1, 2, 3, 4, 5]))

def kwadraty_rec (liczby):
    if len(liczby) == 0: return []
    return [(liczby[0]) ** 2] + kwadraty_rec(liczby[1:])
print(kwadraty_rec([1, 2, 3, 4, 5]))