m=input()
m=list(m)
st=''
for i in range(0,len(m),2):
    m[i],m[i+1]=m[i+1],m[i]
    st+=m[i]+m[i+1]
print(st)
