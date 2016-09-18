n = int(input())
i = 1
st = ''
while (i*i)<(n+1):
    if ((i*i) <= n):
        a = i*i
        st = st + str(a) + ' '
    i = i+1
print(st)