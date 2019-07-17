s=int(input())
f=[]
for i in range(1,s+1):
    if s%i==0:
        f.append(i)
print(*f)
