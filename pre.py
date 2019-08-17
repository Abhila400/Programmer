n=int(input())
a=[]
l=20
for i in range(0,n):
    x=input()
    x=list(x)
    if len(x)<l:
        l=len(x)
    a.append(x)
st=''
f=0
for i in range(0,l):
    if f==0:
        for j in range(1,len(a)):
            if a[0][i]==a[j][i]:
                if j==len(a)-1:
                    st+=a[0][i]
            else:
                f+=1
                break
    else:
        break
print(st)
