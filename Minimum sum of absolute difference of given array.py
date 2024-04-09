arr=[2,5,4,3]
arr.sort()
sum=0
for i in range(len(arr)):
    sum+=abs(arr[i]-arr[i-1])
print(sum)
