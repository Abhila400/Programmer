a=[int(i) for i in input().split()]
n=len(a)
a[0]=a[0]^a[1]
a[1]=a[0]^a[1]
a[0]=a[0]^a[1]
print(*a)
