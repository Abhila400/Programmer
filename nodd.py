m,s=map(int,input().split())
a=[int(i) for i in input().split()]
i=0
while s!=0:
    if a[i]%2!=0:
        m=a[i]
        s-=1
    i+=1
print(m)
