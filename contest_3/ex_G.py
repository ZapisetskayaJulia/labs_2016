a = int(input())
k = 0
n = 0
s = []
while a != 0 :
    s.append(a)
    k +=a
    n +=1
    a = int(input())
av = k/n
l = 0
for i in range(n):
    l=(s[i]-av)**2 + l
print((l/(n-1))**0.5)