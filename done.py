m,s=input().split()
m=list(m)
s=list(s)
r=0
for i in range(0,len(m)):
    if m[i]!=s[i]:
        r+=1
if r==1:
    print('no')
else:
    print('yes')
