s = input()
i = -1
k = 1
if s.count('.') == 3:
    for m in range(1,4):
        a = ''
        i += 1
        while s[i] != '.':
            if s[i] in range(10):
                a = a + s[i]
                i += 1
            else:
                k = 0
        if int(a) >= 256:
            k = 0

    a = ''
    i += 1
    while i <= len(s)-1:
        if s[i] in range(10):
            a = a + s[i]
            i += 1
        else:
            k = 0
    if int(a) >= 256:
        k = 0
else:
    k = 0
if k == 1:
    print( 'YES')
else:
    print('NO')