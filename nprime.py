r=int(input())
flag=0
if r>2:
    for i in range(3,int(r/2)):
        if r%i==0:
            flag=1
            print("no")
            break
if flag==0 or r==2:
    print("yes")
