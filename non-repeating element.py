arr = [1,2,44,3,44,55,55,55]
temp = []
for i in range(len(arr)):
    if arr[i] in temp:
        continue
    else:
        temp.append(arr[i])
        print(temp)
