x = []
y = []
for i in range(8):
    s = input().split()
    x.append(int(s[0]))
    y.append(int(s[1]))
k = 1
for i in range(8):
    for j in range(i + 1, 8):
        if abs(x[i]-x[j]) == abs(y[i] - y[j]):
            k = 0
        if x[i] == x[j]:
            k = 0
        if y[i] == y [j]:
            k = 0
if k == 0:
    print('YES')
else:
    print('NO')
