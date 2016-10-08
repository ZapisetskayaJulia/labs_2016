s = input()
a = s.split('.')
k = 1
for i in range(len(a)):
    if a[i].isdigit() == True:
        if (int(a[i]) > 255) or (int(a[i]) < 0):
            k = 0
    else:
        k = 0
if len(a) != 4:
    k = 0
if k == 1:
    print('YES')
else:
    print('NO')