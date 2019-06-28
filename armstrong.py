a=int(input())
temp=a
sum=0
while a!=0:
    num=a%10
    sum=sum+(num*num*num)
    a=a//10
if sum==temp:
    print("yes")
else:
    print("no")
