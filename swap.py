a=[int(i) for i in input().split()]
n=len(a)
temp=a[0]
a[0]=a[1]
a[1]=temp
print(*a)
