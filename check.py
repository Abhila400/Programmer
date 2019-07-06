n=int(input())
flag=0
for i in range(1,11):
    if n==i:
        flag=1
        print("yes")
        break
if flag==0:
    print("no")
