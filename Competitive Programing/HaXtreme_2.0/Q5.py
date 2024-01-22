
x = int(input().strip()) 
y = int(input().strip()) 
z = list(map(int, input().rstrip().split()))

T=z.copy()
t=x.copy()

u=[]

while(t==0):
    distances = [abs(t - e) for e in T]
    closest = z[distances.index(min(distances))]
    if closest <t:
        t=t-closest
        index = z.index(closest)
        u.append(index)
    else:
        t==t
        T.remove(closest)
u.sort()
for x in range(len(u)):
    print u[x]


