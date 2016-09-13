#task 9
s = input()
for i in range (1,2*len(s),2):
    s = s[:i] + '*' + s[i:]
print (s[:-1])