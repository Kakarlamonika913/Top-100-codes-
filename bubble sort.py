lst=[1,5,3,2,2]
print(lst)
for j in range(len(lst)-1):
    for i in range(len(lst)-1-j):
         if lst[i]>lst[i+1]:
            lst[i],lst[i+1]=lst[i+1],lst[i]
print(lst)
