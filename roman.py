m=input()
l=list(m)
digit=0
a={'I':1,'V':5,'X':10}
for i in range(1,len(l)):
    if a[l[i]]>a[l[i-1]]:
        digit-=a[l[i-1]]
    else:
        digit+=a[l[i-1]]
digit+=a[l[len(l)-1]]
print(digit)
