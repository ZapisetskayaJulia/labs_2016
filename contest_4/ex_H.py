a = int(input())
k = 1
kmax = 1
b = int(input())
if a > b:
    z = 0
if a < b:
    z = 1
if a == b:
    z = 2
    k = 0
while b != 0:
    a = b
    b = int (input())
    if z == 0:
        if a > b:
            z = 0
            k += 1
        if k > kmax:
            kmax = k
        if a < b:
            z = 1
            k = 1
        if a == b:
            z = 2
            k = 0
    if z == 1:
        if a < b:
            z = 0
            k += 1
        if k > kmax:
            kmax = k
        if a > b:
            z = 1
            k = 1
        if a == b:
            z = 2
            k = 0
    if z == 2:
        if a > b:
            z = 0
            k = 1
        if a < b:
            z = 1
            k = 1
        if a == b:
            z = 0
            k = 0
print (kmax)