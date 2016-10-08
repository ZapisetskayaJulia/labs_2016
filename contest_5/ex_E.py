def seq(a):
    a = str(a)
    k = 1
    last = a[0]
    result = ''
    for i in range(1,len(a)):
        if last==a[i]:
            k+=1
        else:
            result = result+str(k)+last
            k=1
        last = a[i]
    result = result+str(k)+last
    return result

a = '1'
k = int(input())
for i in range(k-1):
    a = seq(a)
print(a)