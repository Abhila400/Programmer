n=int(input())
a=[int(i) for i in input().split()]
c=a[0]
for i in range (0,n):
    if a[i]>=c:
        c=a[i]
print(c)
