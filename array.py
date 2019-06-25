n=int(input())
k=int(input())
a=[]
sum=0
for i in range(n):
    x=int(input())
    a.append(x)
for i in range(k):
    sum=sum+a[i]
print(sum)
