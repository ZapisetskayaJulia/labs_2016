a = int(input())
max = 0
k = 1
while a != 0:
    if a == max:
        k += 1
    if a > max:
        k = 1
        max = a
    a = int (input())
print(k)