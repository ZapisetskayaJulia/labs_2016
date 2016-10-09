n = int(input())
s = input().split()
k = 0
for i in range(n-1,-1,-1):
    a = int(s[i])
    if a == 100:
        k += 19
    elif a == 50:
        k += 9
    elif a == 10:
        k += 1
    elif k > 0:
        k -= 1
print(k)