g=int(input())
flag=0
if(g>2):
    for i in range(2,int(g/2)+1):
        if g%i==0:
            print("yes")
            flag=1
            break
if flag==0:
    print("no")
