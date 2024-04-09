arr1=[1,3,2,4]
arr2=[2,1,3,4]
arr1.sort()
arr2.sort(reverse=True)
product=0
for i in range(len(arr1)):
    product+=(arr1[i]*arr2[i])
print(product)
