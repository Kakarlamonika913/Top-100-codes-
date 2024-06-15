a=[1,2,3,4,5]
b=[4,5,6,7,8]
intersection1=[]
union1=a[:]
for i in b:
if i not in a:
union1.append(i)
if i in a:
intersection1.append(i)

print(intersection1)
print(union1)
