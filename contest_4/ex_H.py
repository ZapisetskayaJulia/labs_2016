a = int(input())
k = 2
kmax = 1
b = int(input())
if a > b:
    z = 0
    if b == 0:
        k = 1
if a < b:
    z = 1
if a == b:
    z = 2
    k = 1
a = b
if a == 0:
    print(k)
else:
    b = int(input())
    if k > kmax:
        kmax = k
    while b != 0:
        if z == 0:
            if a > b:
                k += 1
                if k > kmax:
                    kmax = k
            elif a < b:
                z = 1
                k = 2
            elif a == b:
                z = 2
                k = 1
        elif z == 1:
            if a < b:
                k += 1
                if k > kmax:
                    kmax = k
            elif a > b:
                z = 0
                k = 2
            elif a == b:
                z = 2
                k = 1
        elif z == 2:
            if a > b:
                z = 0
                k = 2
            elif a < b:
                z = 1
                k = 2
            elif a == b:
                k = 1
        a = b
        b = int(input())
    print (kmax)