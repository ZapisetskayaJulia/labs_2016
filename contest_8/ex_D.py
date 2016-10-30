s = input().split()
prise = int(s[0])
delta = int(s[1])
m = int(s[2])
week = 0
day = 1
money = 0
while week < m:
    day +=1
    money += prise
    prise += delta
    if day == 8:
        day = 1
        week +=1
print (money)
