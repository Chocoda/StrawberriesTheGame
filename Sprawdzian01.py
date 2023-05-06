import math
# 1. Utworz liste 5 liczb z przedzialu 1 10
# 2. Policz rekurencyjnie ich sume
# 3. Policz iteracyjnie ich iloczyn
# 4. Znajdz rekurencyjnie ich minimum
# 5. Znajdz iteracyjnie ich maksimum
# 6. Utwoz nowa liste (rekurencyjnie lub iteracyjnie) z szescianami liczb z zadanej listy

def suma_rec (liczby):
    if len(liczby) == 0: return 0
    return liczby[0] + suma_rec(liczby[1:])
print(suma_rec([4, 2, 5, 3, 7 ]))

def ilo_iter (liczby):
    iloczyn = 1
    for x in liczby:
        iloczyn *= x
    return iloczyn
print(ilo_iter([4, 2, 5, 3, 7 ]))

def minim_rec (liczby):
    if len(liczby) == 0: return math.inf
    minimum_ogona = minim_rec(liczby[1:])
    if liczby[0] < minimum_ogona:
        return liczby[0]       
    return minimum_ogona
print(minim_rec([4, 2, 5, 3, 7 ]))

def max_iter (liczby):
    maximum = -math.inf
    for x in liczby:
        if x > maximum:
            maximum = x
    return maximum
print(max_iter([4, 2, 5, 3, 7 ]))

def szescian_iter (liczby):
    szescian = []
    for x in liczby:
        szescian.append(x**3)
    return szescian
print(szescian_iter([1, 2, 3, 4]))


lista = ["Ala", "ma", "kota", "i", "psa", "."]

liczby = 0
while liczby < len(lista):
    print(lista[liczby])
    liczby += 2

# [::-1]

def fib_iter(n):
    if n == 0: return 0
    if n == 1: return 1

    prev = 0 # previous
    curr = 1 # current

    for _ in range(n-1):
        tmp = curr # temporary
        curr = curr + prev
        prev = tmp
    return curr

#print([fib_iter(x) for x in range(10)])
print(fib_iter(1000))

def str_without(napis, idx):
    return napis[0:idx] + napis[(idx+1):]
    #return lista
print(str_without("abcdefgh", 2))

def list_without(lista, idx):
    return lista[0:idx] + lista[(idx+1):]
    #return lista

def list_without2(lista, idx):
    retval = []
    for i, v in enumerate(lista):
        if i != idx:
            retval.append(v)
    return retval
def list_without3(lista, idx):
    retval = []
    i = 0
    while i < len(lista):
        if i != idx:
            retval.append(lista[i])
        i += 1
    return retval

print(list_without3(["a", "b", "c", "d", "e"], 2))
# napis abcdefgh 
# str_without(napis, 0) => bcdefgh
# str_without(napis, 1) => acdefgh
# str_without(napis, 2) => abdefgh

def is_symmetrical(napis):
    napis_na_odwrot = napis[::-1]
    if napis == napis_na_odwrot :
        return True
    else: return False

def is_symmetrical2(napis):
    for i in range(len(napis) // 2):
        if napis[i] != napis[len(napis) - 1 - i]:
            return False
    
    return False
    

print(is_symmetrical2("abba"))

# is_symmetric("abba") => True
# is_symmetric("abcba") => True
# is_symmetric("abbd") => False
# is_symmetric("ww") => True
# is_symmetric("aw") => False
# is_symmetric("taggat") => True
# is_symmetric("tagrgat") => True



    