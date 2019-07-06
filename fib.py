n=int(input())
a=[]
a.append(1)
if n==1:
    print(*a)
else:
    a.append(1)
    for i in range (2,n):
        a.append(a[i-1]+a[i-2])
    print(*a)
