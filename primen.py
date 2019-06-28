a=int(input())
b=int(input())
flag=0
for i in range (a+1,b):
    for j in range (2,i):
        if i>2:
            if i%j==0:
                flag=1
                break
        elif i==1 or i==2:
            print(i)
    if flag==0:
        print(i)
