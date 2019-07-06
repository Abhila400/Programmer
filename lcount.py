s=input()
n=len(s)
count=1
for i in range (0,n):
    if s[i]==".":
        count+=1
    else:
        continue
print(count)
