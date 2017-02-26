per = int(input())
q = input().split()
for i in range(per):
    q[i] = q[i][::-1]
q.sort()
for i in range(per):
    q[i] = q[i][::-1]
print(*q)