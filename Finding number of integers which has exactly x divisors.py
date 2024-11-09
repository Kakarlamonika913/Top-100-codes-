n=7
divisior=2
cnt=0
for i in range(1,n+1):
    cnt_fct=0
    for j in range(1,i+1):
        if i%j==0:
            cnt_fct+=1
        else:
            pass
    if cnt_fct==divisior:
        cnt+=1
print(cnt)
