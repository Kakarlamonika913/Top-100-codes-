def check(n,d=None):
    if d is None:
        d=n-1
    while d>=2:
        if n%d==0:
            print("not prime")
            return false
        else:
            return check(n,d-1)
    else:
        print("prime")
        return True
n=int(input())
check(n)
