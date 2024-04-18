arr=[1,2,3,4,5]
n = len(array)
k=2
if n == 0 or k == 0:
    print(array)
    k = k % n
    rotated_array = array[-k:] + array[:-k]
    print( rotated_array)
result=circular_rotate(array, k)
print("Circularly rotated array by", k, "positions:", result)
