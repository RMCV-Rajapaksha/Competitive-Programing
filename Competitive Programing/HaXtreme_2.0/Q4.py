
x = 550
y = 15
z = [44, 400, 33, 567 ,22 ,33 ,45 ,100 ,250 ,50 ,50 ,75 ,34 ,67 ,25]
t=x

t1=[]

p=z.sort(reverse=True)
print(p)

for i in range(len(z)):
    if  z[i]<t:
        t=t-z[i]
        t1.append(i)
