k = 0
a = int(input())
b = int(input())
if b != 0 :
    c = int(input())
    while c!= 0:
        if (a < b) and (b > c):
            k += 1
        a = b
        b = c
        c = int(input())
print (k)