a = int(input())
k1 = 0
k2 = 0
while a != 0:
    if a >= k1:
        k1, k2 = a, k1
    elif a > k2:
        k2 = a
    a = int(input())
print(k2)