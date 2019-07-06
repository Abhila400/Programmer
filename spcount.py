s=input()
n=len(s)
count=0
for i in range (0,n):
    if s[i].isdigit():
        continue
    elif s[i].isalpha() or s[i]==" ":
        continue
    else:
        count+=1
print(count)
