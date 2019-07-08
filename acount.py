n,k=input().split()
count=0
a=[int(i) for i in input().split()]
for i in a:
    if i==int(k):
        count+=1
    else:
        continue
print(count)
