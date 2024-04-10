pairs=[(1,2),(2,1),(3,1),(1,3),(5,4),(4,2)]
s=set()
for(x,y) in pairs:
    s.add((x,y))
    if (y,x) in s:
        print((x,y))
