s=input()
n=len(s)
count=0
for i in range (0,n):
    if s[i].isdigit():
        count+=1
    else:
        continue
print(count)
