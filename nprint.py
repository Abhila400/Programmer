num=int(input())
a=[]
while num!=0:
    a.append(num%10)
    num=num//10
a.reverse()
print(*a)
