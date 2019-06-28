a=[int(i) for i in input().split()]
b=[]
for i in range(a[0]+1,a[1]):
    temp=i
    add=0
    while i!=0:
        num=i%10
        add=add+(num*num*num)
        i=i//10
    if add==temp:
        b.append(add)
print(*b)
