# def liczby(n):
#     i = 0
#     for x in range (n):
#         for y in range (n):
#             i+=1
#             print(f"\t{i}", end="")
#         print()

# def liczby2(n):
#     for i in range (n):
#         for j in range (n):
#             print(f"\t{i*n+j+1}", end="")
#         print()
#         # if x//f ==0: print()
#         # else: print(x, end="")

# liczby2(4)


# def liczby2(w, h):
#     for i in range (h):
#         for j in range (w):
#             print(f"\t{i*w+j+1}", end="")
#         print()
# liczby2(3,4)


# def liczby2(w, h):
#     for i in range (h):
#         for j in range (w):
#             print(f"\t{j*h+i+1}", end="")
#         print()
# liczby2(3,4)

def sums_by_row(numbers, width):
    height = len(numbers) // width
    lista = []
    for row in range(height):
        row_sum = sum(numbers[row*width:(row+1)*width])
        lista.append(row_sum)
        
    return lista


def sums_by_col(numbers, width):
    height = len(numbers) // width
    lista = []

    for col in range(width):
        col_sum = 0
        for row in range(height):
            col_sum += numbers[col + row*width]

        lista.append(col_sum)

    return lista

print(sums_by_row(list(range(1, 13)), 3))
print(sums_by_col(list(range(1, 13)), 3))
