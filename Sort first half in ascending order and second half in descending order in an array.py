arr=[1,3,2,4,5,7,8,9]
mid=len(arr)//2
first_half=sorted(arr[:mid])
second_half=sorted(arr[mid:], reverse=True)
sorted_arr=first_half+second_half
print(sorted_arr)
