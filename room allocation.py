# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    l=map(int,input().split())
    s=0
    for i in l:
        if(i==1):
            s+=1
        elif(i>1):
            if((i%2)==0):
                a=i//2
                s+=a
            elif((i%2)==1):
                b=(i//2)+1
                s+=b
            else:
                pass
            
        else:
            pass
    print(s)            
                
