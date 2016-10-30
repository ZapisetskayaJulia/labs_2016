n = int(input())
b = []
for i in range(n):
    b.append(input())
dic = {}
for i in b:
    if len(i) not in dic:
        dic[len(i)] = [i[::-1]+ ' ' + i]
    else:
        dic[len(i)]+=[(i[::-1] + ' ' + i)]

for i in dic:
    dic[i].sort()

a = dic.keys()
a = list(a)
n = 0
while n < len(a)-1:
     for i in range(len(a)-1-n):
          if (a[i]) > (a[i+1]):
               a[i],a[i+1] = a[i+1],a[i]
     n += 1

for i in a:
    print(i)
    for j in dic[i]:
        print (j)