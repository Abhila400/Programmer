n=int(input())
a=[]
a.append(1)
a.append(1)
for i in range (2,n):
    a.append(a[i-1]+a[i-2])
print(*a)
