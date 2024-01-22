s=list(map(int,input().strip().split()))

n=s[0]
h0=s[1]
a=s[2]
c=s[3]
q=s[4]

data=[h0]

for i in range(1,n):
    num=(a*data[i-1]+c)%q
    data.append(num)

count=0

for j in range(1,n):
    height=0
    for i in range(j-1,-1,-1):
        if data[i]>height:
            height=data[i]
            count+=1

print(count)