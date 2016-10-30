n = 0
while n < len(a)-1:
     for i in range(len(a)-1-n):
          if a[i] > a[i+1]:
               a[i],a[i+1] = a[i+1],a[i]
     n += 1