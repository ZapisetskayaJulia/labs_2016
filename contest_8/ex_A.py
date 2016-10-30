s = input().split()
a_1 = int(s[0],16)
a_2 = int(s[1],16)
print(hex(a_1 ^ a_2)[2:])
