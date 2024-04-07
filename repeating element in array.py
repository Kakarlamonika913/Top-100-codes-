arr=[1,2,2,3,4]
temp=[0]
for i in range(len(arr)):
    if arr[i] in temp:
        print(arr[i])
    else:
        temp.append(arr[i])
        
