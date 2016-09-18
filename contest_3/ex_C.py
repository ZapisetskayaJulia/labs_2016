x = int(input())
p = int(input())
y = int(input())
a = 0
while x < y :
    x = x * (1+p/100)
    x = int(x *100)/100
    a += 1
print(a)