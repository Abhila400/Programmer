import math
num=int(input())
flag=0
if math.ceil(math.log2(num))==math.floor(math.log2(num)):
    print("yes")
else:
    print("no")
