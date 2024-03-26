def findmax(l):
    if (l==[]):
        return None
    max=l[0]
    for i in range(1,len(l)):
        if (l[i]>max):
            max=l[i]
    return max
print(findmax([4,5,62,1]))
            
