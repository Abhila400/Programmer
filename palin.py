c=int(input())
b=c
a=c
r=0
while b!=0:
    a=b%10
    r=r*10+a
    b=b//10
if r==c:
    print("yes")
else:
    print("no")
