ch = int(input())
i = 1
otv = ''
while (i*i)<(ch+1):
    if ((i*i) <= ch):
        a = i*i
        otv = otv + str(a) + ' '
    i = i+1
print(otv)