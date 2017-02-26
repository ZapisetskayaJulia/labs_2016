per = int(input())
a = [0]*per
b = [0]*per
for i in range(per):
    s = input().split()
    a[i] = float(s[0])
    b[i] = float(s[1])

k = 0
while k < len(a)-1:
     for i in range(len(a) - 1 - k):
          if b[i] > b[i + 1]:
               a[i], a[i + 1] = a[i + 1],a[i]
               b[i], b[i + 1] = b[i + 1],b[i]
          elif b[i] == b[i + 1]:
              if a[i] < a[i + 1]:
                  a[i], a[i + 1] = a[i + 1], a[i]
                  b[i], b[i + 1] = b[i + 1], b[i]
     k += 1
for i in range(per):
    print('{0:.2f} {1:.3f}'.format(a[i], b[i]))