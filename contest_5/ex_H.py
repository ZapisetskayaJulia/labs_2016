s = [int(i) for i in input().split()]
n = s[0]
a, b, c, d = s[1], s[2], s[3], s[4]

new = [i for i in range(1,n)]
k = [0 for i in range(n+1)]
for i in range(a,b+1):
    k[i] = i
for i in range(a,b+1):
    new[i] = k[b-i+a]

for i in range (c,d+1):
    k[i] = i
for i in range(c,d+1):
    new[i] = k[d-i+c]
print(*new[::])