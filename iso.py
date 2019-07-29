string=input()
flag=0
for i in string:
	if string.count(i)>1:
		flag=1
		print("No")
		break
if flag==0:
	print("Yes")
