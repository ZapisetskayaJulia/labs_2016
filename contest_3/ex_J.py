fn = int(input())
f1 = 0
f2 = 1
k = 0
a = 0
i = 1
while i<= fn :
    f1, f2 = f2, f1 + f2
    i = f2
    if i == fn :
        a = 1
    k += 1
if a == 1:
    print (k)
else:
    print ('-1')
