c=int(input())
flag=0
if c>2:
    for i in range(2,c):
        if(c%i==0):
            flag=1
            break
else:
    print("yes")
if flag==0:
    print("yes")
else:
    print("no")
