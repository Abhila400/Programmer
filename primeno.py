a=[int(i) for i in input().split()]
b=[]
for i in range (a[0]+1,a[1]):
    flag=0
    for j in range (2,i):
        if i>2:
            if i%j==0:
                flag=1
                break
        else:
            b.append(i)
    if flag==0:
        b.append(i)
print(b)
