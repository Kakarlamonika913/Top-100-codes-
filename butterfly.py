t= int(input())
for _ in range(t):
    r,g,b = map(int, input().split())
    if(r+g < b or r+b < g or b+g < r):
        print("NO")
    else:
        print("YES")
