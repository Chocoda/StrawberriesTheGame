# print("Hello world")
# # for x in range (1,11):
# #     print (str(x) * x)
# fred = "Dlaczego goryle maja wielkie nozdrza? Bo maja wielkie paluchy!!"
# fred01 = "Dlaczego Robin Hood? Bo malo jadl!"
# fred02 = "Jak sie nazywa krzyzowka weza z jezem? Drut kolczasty!"
# fred03 = 'Wyznala mi "nocami czytuje "Pythona dla dzieciakow""'
# print(f"{fred}, ")
# lista_czarodzieja = ["nogi pajaka", "zabi plalec", "oko traszki", "skrzydlo nietoperza", "maslo z pomrowika, lupiez weza"]
# print(lista_czarodzieja[2:7])

# def row_maj_print_matrix(numbers, width):
#     height = len(numbers)// width
#     for row in range (height):
#         for col in range (width):
#             print(numbers[col+width*row], end="")
#         print("")

# def col_maj_print_matrix(numbers, width):
#     height = len(numbers)// width
#     for row in range (height):
#         for col in range (width):
#             print(numbers[row+col*height], end="")
#         print("")

# def rm2cm(numbers, width):
#     height = len(numbers)// width
#     new_lista = [None]*len(numbers)

#     for row in range (height):
#         for col in range (width):
#             new_lista[row + height*col] = numbers[col + width*row]

#     return new_lista

# def cm2rm(numbers, width):
#     height = len(numbers)// width
#     new_lista = [None]*len(numbers)
#     for row in range (height):
#         for col in range (width):
#             new_lista[col + width* row] = numbers[row + height*col]

#     return new_lista
    

# rm_lista = [chr(ord("a") + i) for i in range(12)]
# cm_lista = [chr(ord("a")+ 3*(i%4) + i // 4) for i in range(12)]
# # print(rm_lista)
# # print(cm_lista)

# # row_maj_print_matrix(rm_lista, 3)
# # print()
# # col_maj_print_matrix(cm_lista, 3)
# # print()
# print(rm2cm(rm_lista, 3))
# col_maj_print_matrix(rm2cm(rm_lista, 3), 3)
# print("---------")
# row_maj_print_matrix(cm2rm(cm_lista, 3), 3)
# print("---------")
# #print(cm2rm(cm_lista, 3))

# week = ["mon", "tue", "wen", "thu", "fri", "sat", "sun"]

# print(168745257552%360)

# def trace(matrix, width):
#     height = len(matrix) // width

#     if width != height:
#         return None

#     suma = 0

#     for i in range(width):
#         suma += matrix[i*width + i]
    
#     return suma




# print(trace([7, 5, 2, 4, 3, 1, 5, 4, 13], 3)) # 13

def rm_row_sums(matrix, width):
    height = len(matrix)// width
    lista = [None] * height

    for row in range (height):
        suma = 0
        for col in range (width):
            suma += matrix[col+row*width]
        lista [row] = suma

    return lista
            

def rm_col_sums(matrix, width):
    height = len(matrix)// width
    lista = [None] * width

    for col in range (width):
        suma = 0
        for row in range (height):
            suma += matrix[col+row*width]
        lista [col] = suma

    return lista

def cm_row_sums(matrix, width):
    height = len(matrix)// width
    lista = [None] * height
    for row in range (height):
        suma = 0
        for col in range (width):
            suma += matrix[row+col*height]
        lista [row] = suma

    return lista

def cm_col_sums(matrix, width):
    height = len(matrix)// width
    lista = [None] * width
    for col in range (width):
        suma = 0
        for row in range (height):
            suma += matrix[row+col*height]
        lista [col] = suma

    return lista


rm_lista3na4 = [_ for _ in range(1, 13)] # width = 3
cm_lista3na4 = [3*(i%4) + 1 + i // 4 for i in range(12)] # width = 3
# print(cm_lista3na4)
# print(rm_row_sums(rm_lista3na4, 3))
# print(rm_col_sums(rm_lista3na4, 3))

print(cm_row_sums(cm_lista3na4, 3))
print(cm_col_sums(cm_lista3na4, 3))