f,l=map(int,input().split())
a=list(range(f,l+1))
m=2
while m<=int(l/2):
    for i in range(2,int(l/m)+1):
        if m*i in a:
            a.remove(m*i)
    m+=1
print(len(a))
