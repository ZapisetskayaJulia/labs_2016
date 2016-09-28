a = int(input())
last = 0
k = 0
kmax = 1

while a != 0:
    if last == a:
        k += 1
        if k > kmax:
            kmax = k
    else:
        k = 1
        last = a
    a = int(input())
print (kmax)