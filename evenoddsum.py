def evenoddsum(lst):
    even_sum=0
    odd_sum=0
    for i in lst:
        if i%2==0:
            even_sum+=i
        else:
            odd_sum+=i
    return even_sum,odd_sum
lst=[1,2,3,4]
evenoddsum(lst)
        
