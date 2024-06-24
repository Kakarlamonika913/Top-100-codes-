k=int(input(‘enter k value’))
a=list(map(int,input().split()))
n=len(a)
def findkmax(k,a):
for i in range(n):
for j in range(0,n-1-i):
if a[j]a[j+1]:
a[j],a[j+1]=a[j+1],a[j]
print(a)
print(‘kin element’,a[k-1])

findkmax(k,a)
findkmin(k,a)
