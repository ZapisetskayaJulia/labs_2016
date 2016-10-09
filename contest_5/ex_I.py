n = int(input())
x =[0]*n
y =[0]*n
for i in range(n):
    s = input().split()
    x[i], y[i] = [int(j) for j in s]
max = 0
for i in range (n):
    for j in range(i + 1, n):
        if abs(((x[i]-x[j])**2 + (x[i]-x[j])**2))**(1/2) > max:
            max = abs(((x[i]-x[j])**2 + (x[i]-x[j])**2))**(1/2)
print(max)