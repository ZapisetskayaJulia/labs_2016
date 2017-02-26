s1 = input().split('.')
s2 = s1[0]
a = [i for i in s2 ]
kol = 0
while kol < len(a)-1:
     for i in range(len(a) - 1 - kol):
          if ord(a[i]) > ord(a[i + 1]):
               a[i],a[i + 1] = a[i + 1],a[i]
     kol += 1
print(''.join(a), '.',sep='' )