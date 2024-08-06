def intreverse(n):
    sum=0
    while(n>0):
      rem=n%10
      sum=sum*10+rem
      n=n//10
    return(sum)
def matched(s):
    n=len(s)
    stack=[]
    for i in range(n):
        if s[i]=='(':
           stack.append([i])
        elif s[i]==')':
            if stack:
              stack.pop()
            else:
              return False
    if stack:
       return False
    return True
def prime(n):
  f=0
  for i in range(2,n):
    if n%i==0:
       f=1
       break
  if f==0:
     return True
  return False
def sumprimes(l):
    sum=0
    for i in range(len(l)):
      if l[i]>0 and prime(l[i]):
        sum=sum+l[i]
    return sum



          
        
  
