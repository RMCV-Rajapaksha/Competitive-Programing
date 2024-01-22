n,m = list(map(int,input().split()))

scheme=[]
poem=[]

for _ in range(n):
    scheme.append(tuple(map(str,input().split())))
input()
for _ in range(1,m*2+1,2):
    poem.append(list(map(str,input().split()))[-1])


