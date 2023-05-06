import math

def max_value(float_list):
    max_v = -math.inf

    for x in float_list:
        if x > max_v:
            max_v = x
    
    return max_v

def min_value(float_list):
    min_v = math.inf

    for x in float_list:
        if x < min_v:
            min_v = x
    return min_v


def mean_value(float_list):
    suma = 0
    for x in float_list:
        suma += x
    mean_value = suma / len(float_list)
    return mean_value


def geom_mean(float_list):
    iloczyn = 1
    for x in float_list:
        iloczyn *= x
    geom_mean = iloczyn ** (1/len(float_list))
    return geom_mean



    
    
# mean_v = sum(float_list) / len(float_list)
# return mean_v

def vector_norm(float_list):
    suma = 0
    for x in float_list :
        product = x * x
        suma += product
    vector_norm = suma ** (1/2)
    return vector_norm


print(max_value([-100]))
print(max_value([]))

print(min_value([-2, 4, 1, -4.1, 3]))
print(mean_value([-2, 4, 1, 4.1, 3]))
print(geom_mean([2, 4, 1, 4.1, 3]))
print(vector_norm([1, -2, 2]))





import math

def max_value1(float_list):
    max_v = -math.inf
    for x in float_list:
        if x > max_v :
            max_v = x
    return max_v

print(max_value1([-2, 4, 1, -4.1, 3]))

