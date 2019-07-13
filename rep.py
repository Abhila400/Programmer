g=input()
n=len(g)
if n%2!=0:
    a=g.replace(g[int(n/2)],'*',1)
else:
    c=g.replace(g[int(n/2)-1],'*',1)
    a=c.replace(c[int(n/2)],'*',1)
print(a)
