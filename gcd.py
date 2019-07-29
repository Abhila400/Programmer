mahi,sakshi=input().split()
mahi=int(mahi)
sakshi=int(sakshi)
min=mahi
if mahi>sakshi:
	min=sakshi
gcd=1
for i in range(2,min+1):
	if mahi%i==0 and sakshi%i==0:
		gcd=i
print(gcd)
