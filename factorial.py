a=int(input())
factorial=1
if a>0:
    for i in range(1,a+1):
        factorial=factorial*i
    print(factorial)
else:
    factorial=1
    print(factorial)
