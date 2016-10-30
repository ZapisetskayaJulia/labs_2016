k = int(input())
s = input().split()
a = [i for i in s]
for i in range(len(a)):
    a[i] = a[i][::-1]
n = 0
while n < len(a)-1:
     for i in range(len(a)-1-n):
          if a[i] > a[i+1]:
               a[i],a[i+1] = a[i+1],a[i]
     n += 1
for i in range(len(a)):
    a[i] = a[i][::-1]
n = 0
print(*a)