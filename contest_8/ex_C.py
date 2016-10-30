n = int(input())
s = input().split()
a = [int(i) for i in s]
b = [0]*n
b[n-1] = 1
for i in range(n-1,-1,-1):
    b[i-1] = b[i]^a[i]
    if b[i-1]==1:
        b[i-1] = 0
    else:
        b[i-1] = 1
min_r = b.count(1)
min_l = b.count(0)
print(min(min_r,min_l))