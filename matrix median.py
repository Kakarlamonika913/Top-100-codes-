def median_matrix(a):
    if len(a)==1:
        vec=a[0]
        return vec[len(vec)//2]
    else:
        new_list=[]
        for row in range(len(a)):
            new_list.extend(a[row])
        new_list=sorted(new_list)
    return new_list[len(new_list)//2]
l1=[1,3,5]
l2=[2,6,9]
l3=[3,6,9]
a=[l1,l2,l3]
print(median_matrix(a))
