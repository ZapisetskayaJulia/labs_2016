cur=int(input())
ch1=0
ch2=1
num=0
a=0
i=1
while i<=cur:
    ch1, ch2=ch2, ch1+ch2
    i=ch2
    if i == cur :
        a = 1
    num += 1
if a == 1:
    print (num)
else:
    print ('-1')
