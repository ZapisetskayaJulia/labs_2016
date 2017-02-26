per = int(input())
a = [int(s) for s in input().split()]
b = [0]*per
b[per-1] = 1
for i in range(per-1, -1, -1):
    b[i-1] = b[i]^a[i]
    if b[i-1] == 1:
        b[i-1] = 0
    else:
        b[i-1] = 1
print(min(b.count(1), b.count(0)))