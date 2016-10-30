s_1 = input().split('.')
s = s_1[0]
a = [i for i in s ]
n = 0
while n < len(a)-1:
     for i in range(len(a)-1-n):
          if ord(a[i]) > ord(a[i+1]):
               a[i],a[i+1] = a[i+1],a[i]
     n += 1
print(''.join(a), '.',sep='' )