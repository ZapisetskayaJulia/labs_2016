s = input().split()

prise = int(s[0])
delta = int(s[1])
m = int(s[2])

week = 0
summa = 0
day = 1

while week < m:
    day +=1
    summa += prise
    prise += delta
    if day == 8:
        day = 1
        week +=1
print(summa)
