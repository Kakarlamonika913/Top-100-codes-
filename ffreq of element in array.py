arr=[1,2,3,4,2,3]
freq={}
for i in  arr:
    if i in freq:
        freq[i]+=1
    else:
        freq=1
    print(freq)
