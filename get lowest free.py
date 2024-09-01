sale= int(input())
for s in range(sale):
  a=list(map(int,input().split()))
  print(sum(a)-min(a))
