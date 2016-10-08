s = input()
x = 0
y = 0
while s != 'Treasure!':
    k = s.index(' ')
    if s[:k] == 'North':
        y += int(s[(k+1):])
    elif s[:k] == 'South':
        y -= int(s[(k + 1):])
    elif s[:k] == 'East':
        x += int(s[(k + 1):])
    elif s[:k] == 'West':
        x -= int(s[(k + 1):])
    s = input()
print(x,y)
