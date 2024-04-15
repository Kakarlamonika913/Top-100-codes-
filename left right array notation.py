arr=[1,2,3,4,5,6]
def left(arr,p):
for i in range(0,p):
x=arr[0]
arr.remove(x)
arr.append(x)
return arr
print(left(arr,3)
