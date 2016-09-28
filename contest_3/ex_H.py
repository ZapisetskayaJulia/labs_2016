cur1=int(input())
cur2=int(input())
sum=0
while (cur1 != 0) or (cur2 !=0):
    sum +=cur1
    cur1=cur2
    cur2= int(input())
print(sum)