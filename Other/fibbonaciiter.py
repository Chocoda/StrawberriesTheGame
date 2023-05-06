import time

def fib_rec(n):
    if n == 0 or n == 1: return n

    return fib_rec(n - 1) + fib_rec(n - 2)

def fib(n):
    if n == 0: return 0
    if n == 1: return 1
    a = 0
    b = 1
    for x in range(n-1):
        c = a + b
        a = b
        b = c
    return b

def fib2(n):
    current_value = 0
    next_value = 1
    for i in range(n):
        tmp = current_value + next_value
        current_value = next_value
        next_value = tmp

    return current_value

# def fib(n):
#     # Warunki stopu
#     if n == 0: return 0
#     if n == 1: return 1

#     # CVzesc rekurencyjna
#     return fib(n-1) + fib(n-2)


fib_input = 5000
print(f"Iteracyjnie dla {fib_input}: {fib2(fib_input)}")


fib_input = 33

# start_time = time.perf_counter()
# print(fib_rec(fib_input))
# fib_rec_time_diff = time.perf_counter() - start_time
# print(f"fib_rec time: {fib_rec_time_diff}")

start_time = time.perf_counter()
print(fib2(fib_input))
fib_itr_time_diff = time.perf_counter() - start_time
print(f"fib_itr time: {fib_itr_time_diff}")


# print([fib(x) for x in range(10)])# = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
# print([fib2(x) for x in range(10)])
