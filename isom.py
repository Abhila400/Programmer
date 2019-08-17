m,s=input().split()
m=list(m)
s=list(s)
flag=0
pattern=ord(m[0])-ord(s[0])
for i in range(1,len(m)):
    if ord(m[i])!=ord(s[i])+pattern:
        flag=1
        print('no')
        break
if flag==0:
    print('yes')
