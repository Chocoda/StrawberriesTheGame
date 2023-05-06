def fibb (n):
    if n == 0 : return 0
    if n ==1 : return 1
    return fibb(n-1) + fibb(n-2)

print(fibb(10))

def rec_sum( float_list):
    if len(float_list) == 1 : return float_list[0]
    return float_list[0] + rec_sum(float_list[1:])


print(rec_sum([1, 2, 3]))

lista = list(range(10))
print(lista)
indeks_elementu_do_pominiecia = 4
print(lista[:indeks_elementu_do_pominiecia])
print(lista[indeks_elementu_do_pominiecia+1:])
print(lista[:indeks_elementu_do_pominiecia] + lista[indeks_elementu_do_pominiecia+1:])


a = 3
b = 7

