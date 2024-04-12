 a=[11,200,22,47,66]
s=a.copy()
s.sort() l=[]
for i in range(len(a)):
for j in range(len(s)):
if a[i]==s[j]:
l.append(j+1)
print(l)
