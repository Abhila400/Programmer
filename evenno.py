a=[int(i) for i in input().split()]
b=[]
for i in range (a[0]+1,a[1]):
    if i%2==0:
        b.append(i)
print(*b)
