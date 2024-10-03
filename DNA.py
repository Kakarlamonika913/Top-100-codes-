line=int(input())
for l in range(line):
  x,y=map(int,input().split())
  med=(x+y)//2
  chef=abs(med-x)
  chefina=abs(med-y)
  print(max(chef,chefina))
