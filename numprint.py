number=int(input())
arr=[]
while number!=0:
    arr.append(number%10)
    number=number//10
arr.reverse()
print(*arr)
