n,k=input().split()
flag=0
a=[int(i) for i in input().split()]
for i in a:
    if i==int(k):
        flag=1
        break
if flag==1:
    print("yes")
else:
    print("no")
