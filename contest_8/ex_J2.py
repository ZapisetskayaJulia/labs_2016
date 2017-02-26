cur = int(input())
a =[]
for i in range(cur):
    s = input()
    a.append([s,s[::-1], len(s)])
for j in range(cur):
    for i in range(cur-1):
        if a[i][2] > a[i + 1][2]:
            a[i],a[i + 1] = a[i + 1],a[i]
for j in range(cur):
    for i in range(cur-1):
        l = min(a[i][2],a[i + 1][2])
        sr = False
        for k in range(l):
            if ord(a[i][1][k]) > ord(a[i + 1][1][k]) and a[i][2] == a[i + 1][2] and not sr:
                a[i],a[i+1] = a[i + 1],a[i]
                sr = True
            elif ord(a[i][1][k]) < ord(a[i + 1][1][k]) and a[i][2] == a[i + 1][2] and not sr:
                sr = True
print(a[0][2])
print(a[0][1],a[0][0])
for i in range(1, cur):
    if a[i][2] == a[i - 1][2]:
        print(a[i][1],a[i][0])
    else:
        print(a[i][2])
        print(a[i][1],a[i][0])