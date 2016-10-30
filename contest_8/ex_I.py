k = int(input())
a = [0]*k
b = [0]*k
for i in range(k):
    s = input().split()
    a[i] = float(s[0])
    b[i] = float(s[1])

n = 0
while n < len(a)-1:
     for i in range(len(a)-1-n):
          if b[i] > b[i+1]:
               a[i], a[i+1] = a[i+1],a[i]
               b[i], b[i + 1] = b[i + 1],b[i]
          elif b[i] == b[i+1]:
              if a[i] < a[i + 1]:
                  a[i], a[i + 1] = a[i + 1], a[i]
                  b[i], b[i + 1] = b[i + 1], b[i]
     n += 1
for i in range(k):
    print('{0:.2f} {1:.3f}'.format(a[i], b[i]))