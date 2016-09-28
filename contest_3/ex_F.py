cur=int(input())
kol=0
sum=0
while cur != 0 :
    sum=sum+cur
    kol +=1
    cur=int(input())
print(sum/kol)