a = 0
b = 1
n = int(input())
if n == 0:
    print(a)
if n == 1:
    print (b)
if n!=0 and n!=1 :
    for i in range(2,n+1):
        a, b = b, a+b
    print (b)