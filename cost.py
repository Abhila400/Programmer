m,s=input().split()
m=list(m)
s=list(s)
c=0
l=max(len(m),len(s))
for i in range(0,l):
    if i<len(m):
        if m[i]==s[i]:
            continue
        else:
            c+=1
    else:
        c+=1
print(c)
