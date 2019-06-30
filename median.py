import math
n=int(input())
a=[int(i) for i in input().split()]
a.sort()
if n%2!=0:
    median=a[(n-1)//2]
else:
    median=math.ceil((a[(n-1)//2]+a[n//2])/2)
print(median)
