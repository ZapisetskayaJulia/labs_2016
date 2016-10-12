import random
import numpy as np
import matplotlib.pyplot as plt


def get_percentile(values, bn):
    k = 100/bn
    s = [0.0]
    for i in range(1, bn):
        s.append(np.percentile(values, k*i))
    return s

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bn = int(input())
spisok = get_percentile(values,bn)
print(get_percentile(values,bn))


def get_percentile_number (a,percentiles):
    i = 0
    while (percentiles[i] <= a) and(i < len(percentiles)):
        i += 1
    return i-1
k_1 = float (input())
numb = get_percentile_number(k_1, spisok)
print(numb)


def value_equalization(value, percentiles):
    idx = get_percentile_number(value,percentiles)
    step = 1/len(percentiles)
    new_value = idx*step
    return new_value
print(value_equalization(k_1,spisok))


def value_equalization(value, percentiles,add_random=False):
    idx = get_percentile_number(value,percentiles)
    step = 1/len(percentiles)
    if add_random:
        random_noise = random.random()
        new_value = step*(idx+random_noise)
    else:
        new_value = idx*step
    return new_value
add_random = int(input())
print(value_equalization(k_1,spisok,add_random))