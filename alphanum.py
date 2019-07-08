string=input()
n=len(string)
digit=0
alpha=0
for i in range(0,n):
    if string[i].isdigit():
        digit=1
        break
for i in range(0,n):
    if string[i].isalpha():
        alpha=1
        break
if digit==1 and alpha==1:
    print("Yes")
else:
    print("No")
