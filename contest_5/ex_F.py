n = int(input())
s = input().split()
a = [int(i) for i in s]  #a = [int(i) for i in input().split()]
min = abs(a[1] - a[0])
k_1 = 0
k_2 = 1
for i in range (len(a)):
    for j in range(i + 1, len(a)):
        if abs(a[i]-a[j]) < min:
            min = abs(a[i]-a[j])
            k_1 = i
            k_2 = j
print(k_1, k_2)