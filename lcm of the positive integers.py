def find_lcm(x,y):
    max=x if x>y else y
    while True:
        if max%x==0 and max%y==0:
            return max
        max+=1
a=int(input())
b=int(input())
lcm_result=find_lcm(a,b)
print(lcm_result)
