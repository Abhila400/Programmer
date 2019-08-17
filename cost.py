m,s=input().split()
m=list(m)
s=list(s)
c=0
if len(m)<len(s):
    for i in range(0,len(s)):
        if i<len(m):
            if m[i]==s[i]:
                continue
            else:
                c+=1
        else:
            c+=1
else:
    for i in range(0,len(m)):
        if len(m)>len(s):
            m.pop()
            c+=1
        else:
            break
    for i in range(0,len(s)):
        if m[i]!=s[i]:
            c+=1
print(c)
