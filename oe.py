mahi=input()
a=1
b=""
c=""
for i in mahi:
    if a%2==0:
        b+=i
    else:
        c+=i
    a+=1
print(c,b)
