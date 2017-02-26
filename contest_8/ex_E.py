s = input()
c = 0
T = True
for i in range(len(s)):
    if s[i:i+1] == '(':
        c +=1
    if s[i:i+1] == ')':
        c -=1
        if c < 0:
            T = False
if (T == True) and (c == 0):
    print('YES')
else:
    print('NO')