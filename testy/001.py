"""REKURENCJA ILOCZYN"""
def il_rec(liczby):
    if len(liczby) == 0: return 1
    return liczby[0] * il_rec(liczby[1:])

print(il_rec([4, 2, 3]))

"""MINIMUM ITERACJA"""

import math
def min_iter(liczby):
    min_val = math.inf
    for x in liczby :
        if x < min_val:
            min_val = x
    return min_val
print(min_iter([4, 2, 3]))

"FIBONACCI"
def fibb (f):
    if f == 0: return 0
    if f == 1: return 1
    return fibb(f-1)+ fibb(f-2)
print([fibb(x) for x in range(10)])

"""
"CZWICZENIE"
mozliwe_odpowiedzi = ["a", "b", "c", "d"]
def abcd_question(pytanie, opcje, praw_odp):
    while True:
        print(pytanie)
        for i, v in enumerate(opcje):
            print(f"\t{mozliwe_odpowiedzi[i]}. {v}") 
        odp = input().lower()
        if odp in mozliwe_odpowiedzi:
            if odp == praw_odp.lower():
                return 1
            else:
                return 0

pytania = [
    ["Stolica Polski?", ["Krakow", "Warszawa", "Poznan", "Gdansk"], "b"],
    ["Stolica Francji?", ["Paryz", "Gdynia", "Poznan", "Gdansk"], "a"],
    ["Stolica Hiszpanii?", ["Krakow", "Warszawa", "Poznan", "Madryt"], "d"],
    ["Stolica Wloch?", ["Krakow", "Warszawa", "Rzym", "Gdansk"], "c"]
]
score = 0
for lista_z_pytaniem in pytania:
    score += abcd_question(*lista_z_pytaniem) 

print(f"Prawidlowe odpowiedzi: {score}/{len(pytania)}")
print(f"Procent prawidlowych odpowiedzi: {100*score/len(pytania)}%")
"""
"SILNIA"
def facrec(n):
    if n == 0 : return 1
    return n * facrec(n-1)

print(facrec(5)) 

"SILNIA ITER"
def faciter(n):
    silnia = 1
    for x in range (1, n+1):
        silnia *= x
    return silnia
print(faciter(5)) 


"QUIZ"
print("Zobaczymy jak sie znasz na datach")
mozliwe_odpowiedzi = ["a", "b", "c", "d"]
def quiz_question(pytanie, opcje, praw_odp):
    while True:
        print(pytanie)
        for i, v in enumerate(opcje):
            print(f"\t{mozliwe_odpowiedzi[i]}. {v}") 
        odp = input().lower()
        if odp in mozliwe_odpowiedzi:
            if odp == praw_odp.lower():
                return 1
            else:
                return 0

pytania = [
    ["Kiedy skonczyla sie druga wojna swiatowa?", ["1815", "1872", "1899", "1799"], "a"],
    ["Poczatek drugiej wojny swiatowej?", ["2017", "1914", "1939", "1895"], "c"],
    ["Wojna na Ukrainie", ["1203", "2013", "2023", "2022"], "d"],
    ["Narodziny Jezusa?", ["2019", "0", "100", "-1"], "b"],
    ["Smierc Krolowej Elzbiety II?", ["1275", "1899", "2022", "2021"], "c"]
]
score = 0
for lista_z_pytaniem in pytania:
    score += quiz_question(*lista_z_pytaniem) 

print(f"Prawidlowe odpowiedzi: {score}/{len(pytania)}")
if score >= 7 :
    print("Udalo ci sie!")
else:
    print("Nie martw kiedys ci sie uda (mam nadzieje)")

