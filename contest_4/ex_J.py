k = 0
a = int(input())
b = int(input())
kmin = -1
if b != 0 :
    c = int(input())
    while c!= 0:
        if (a < b) and (b > c):
            if (k < kmin) and ( kmin != -1):
                kmin = k
            elif kmin == -1:
                kmin = 2500000
            k = 1
        else:
            k += 1
        a = b
        b = c
        c = int(input())
if (kmin == 2500000) or (kmin == -1):
    print('0')
else:
    print (kmin)