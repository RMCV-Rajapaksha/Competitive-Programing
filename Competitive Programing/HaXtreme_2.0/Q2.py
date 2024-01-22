
x = int(input().strip()) 
y = list(map(int, input().rstrip().split())) 

h=y[0]
h1=0
s1=0
f1=0
i1=0
i2=0
i3=0

for i in range(1,len(y)):
    if y[i]>h:
        h=y[i]
        h1=h1+1
        i1=i
    elif y[i]<h:
        h=y[i]
        s1=s1+1
        i2=i
    elif y[i]==h:
        h=y[i]
        f1=f1+1
        i3=i



    
    

