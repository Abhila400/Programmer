s=int(input())
a=[]
while s!=0:
    r=s%10
    if r%2!=0:
        a.append(r)
    s=s//10
a=a[::-1]
print(*a)
