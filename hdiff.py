a=[int(i) for i in input().split()]
b=[int(i) for i in input().split()]
minsa=a[0]*60+a[1]
minsb=b[0]*60+b[1]
if minsa>minsb:
    m=minsa-minsb
else:
    m=minsb-minsa
hrs=m//60
mins=m%60
print(hrs,mins)
