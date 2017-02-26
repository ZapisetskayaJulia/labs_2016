s = input().split()
n1 = int(s[0],16)
n2 = int(s[1],16)
print(hex(n1 ^ n2)[2:])
