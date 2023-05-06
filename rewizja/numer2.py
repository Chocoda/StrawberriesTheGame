def suma (liczby):
    suma = 0
    for i in liczby:
        suma += i
    return suma
print(suma([1,3,5]))

def suma_rec (liczby):
    if len(liczby) == 0: return 0
    return liczby[0] + suma_rec(liczby[1:])
print(suma_rec([1,3,5]))  

import math
def minimum_iter (liczby):
    minimum = math.inf 
    for x in liczby:
        if x < minimum:
            minimum = x
    return minimum
print(minimum_iter([1,3,5])) 

import math
def minimum_rec (liczby):
    if len(liczby) == 0: return math.inf
    minimum_ogona = minimum_rec(liczby[1:])
    if liczby[0]< minimum_ogona:
        return liczby[0]
    return minimum_ogona
print(minimum_rec([1,3,5])) 

def silnia_iter (i):
    silnia = 1
    for x in range (1, i+1):
        silnia *= x
    return silnia
print(silnia_iter(5)) 

def silnia_rec(i):
    if i==0 : return 1
    return i * silnia_rec(i-1)
print(silnia_rec(5)) 

def fibonacci (n):
    if n== 0: return 0
    if n==1 : return 1
    return fibonacci(n-1) + fibonacci(n-2)
print([fibonacci(x)for x in range(10)])

def kwadraty_iter(liczby):
    kwadraty = []
    for x in liczby:
        kwadraty.append(x**2)
    return kwadraty
print(kwadraty_iter([1,2,3,4,5]))

def kwadraty_rec(liczby):
    if len(liczby)== 0: return []
    return [(liczby[0]) ** 2] + kwadraty_rec(liczby[1:])

print(kwadraty_rec([1,2,3,4,5]))
