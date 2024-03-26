def findmin(l):
    if (l==[]):
        return None
    min=l[0]
    for i in range(1,len(l)):
        if (l[i]<min):
            min=l[i]
    return min
print(findmin([4,5,62,1]))
            
