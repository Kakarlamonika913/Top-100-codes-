arr=list(map(int,input().split()))
sum=1
for i in range(len(arr)):
if arr[i]==0:
pass
else:sum*=arr[i]
print(abs(sum))
