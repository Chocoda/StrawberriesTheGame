import math

def geom_mean(float_list):
    product = 1
    for x in float_list:
        product *= x
    geom_mean = product ** (1/ len (float_list))
    return geom_mean

def maximum(float_list):
    max_val = -math.inf
    for x in float_list:
        if x > max_val:
            max_val = x
    return max_val
       


print((440*1760)**.5)

print(geom_mean([-2, 3, 4.8, -2.1]))
print(maximum([-2, 3, 4.8, -2.1]))
