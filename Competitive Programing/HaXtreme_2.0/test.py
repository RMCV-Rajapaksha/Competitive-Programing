

import copy

x=550
y=15
z=[44,400 ,33, 567, 22, 33 ,45 ,100 ,250 ,50 ,50 ,75, 34 ,67 ,25]

T=z.copy()
t=x

u=[]

while(t>0):
    distances = [abs(t - e) for e in T]
    closest = T[distances.index(min(distances))]
    if closest <=t:
        t=t-closest
        index = z.index(closest)
        u.append(index)
    else:
        
        T.remove(closest)
u.sort()
print(*u)

