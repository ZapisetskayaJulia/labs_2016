s = input()
if s[1] == ':':
    h = '0'+ s[0]
    min = s[2]+s[3]
if s[2] == ':':
    h = s[0]+ s[1]
    min = s[3]+ s[4]
if s[-4] == 'a':
    if h == '12':
        h = '00'
    s_new = h + ':' + min
else:
    if h == '12':
        h_new = 12
    else:
        h_new = int (h) + 12
    s_new = str(h_new) + ':' + min
print(s_new)