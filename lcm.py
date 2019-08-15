mahi,sakshi=input().split()
mahi=int(mahi)
sakshi=int(sakshi)
min=mahi
if mahi>sakshi:
	min=sakshi
lcm=1
for i in range(1,min+1):
	if mahi%i==0 and sakshi%i==0:
		l=mahi/i
		lcm=l*sakshi
print(int(lcm))
