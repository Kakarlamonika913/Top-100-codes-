arr=[1,2,3,4,5]
n=len(arr)
counteven=0
countodd=0
for i in range(0,n):
    if arr[i]%2==0:
        counteven+=1
    else:
        countodd+=1
print(counteven)
print(countodd)
