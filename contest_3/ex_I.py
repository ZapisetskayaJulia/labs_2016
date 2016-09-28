ch1=0
ch2=1
n=int(input())
if n == 0:
    print (ch1)
if n == 1:
    print (ch2)
if (n!=0) and (n!=1) :
    for i in range(2,n+1):
        ch1, ch2=ch2, ch1+ch2
    print (ch2)