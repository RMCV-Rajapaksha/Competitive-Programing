from itertools import permutations

n=int(input())

d=str(input())
l =[x for x in range(1,n+1)]

p=permutations(l)

ans=0

co=0

for i in list(p):
    for j in range(0,len(i)-1):
        if d[j]==">" and i[j]>i[j+1]:
            co+=1
        elif d[j]=="<" and i[j]<i[j+1]:
            co+=1
    if co==n-1:
        ans+=1
    co=0

print(ans)