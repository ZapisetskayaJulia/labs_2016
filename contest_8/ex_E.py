s = input()
cnt = 0
a = True
for i in range(len(s)):
    if s[i:i+1] == '(':
        cnt +=1
    if s[i:i+1] == ')':
        cnt -=1
        if cnt < 0:
            a = False
if (a == True) and (cnt == 0):
    print('YES')
else:
    print('NO')