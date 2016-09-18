a = int(input())
b = int(input())
k = 0
while (a != 0) or (b !=0):
    k +=a
    a = b
    b = int(input())
print(k)