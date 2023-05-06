"""
def suma_iter(float_list):
    sum_val = 0
    for x in float_list:
        sum_val += x
    return sum_val

def suma_req(float_list):
    if len(float_list) == 1: return float_list[0]

    return float_list[0] + suma_req(float_list[1:])

print(suma_iter([1, 2, 3]))
print(suma_req([1, 2, 3]))
"""
"""
def pr_inc():
    print(pr_inc.i)
    pr_inc.i += 1
pr_inc.i = 1
"""
""" pr_inc()"""
  
def fibb(n):
    if n == 0: return 0
    if n == 1: return 1
    return fibb(n-1) + fibb(n-2)


# fibbonaci = fibb(10) + fibb(5)
print(f"wynik = {fibb(20)}")














def fibb(n):
    if n == 0 : return 0
    if n == 1: return 1
    return fibb(n- 1) + fibb(n-2)





print(f"wynik = {fibb(20)}")