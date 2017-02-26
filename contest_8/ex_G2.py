cur = input()
a = []
r = ''
n = cur.find('.')
for i in range(n):
    a.append(cur[i])
for i in range(n):
    for j in range(n-1):
        if ord(a[j])>ord(a[j+1]):
            a[j], a[j+1] = a[j+1], a[j]
for i in range(n):
    r += str(a[i])
r += '.'
print(r)