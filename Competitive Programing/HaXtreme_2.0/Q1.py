
x = int(input().strip()) 
y = list(map(int, input().rstrip().split())) 

h=0
hill=[]
slope =[]
flat =[]

for i in range(x):
    if h<y[i]:
        h=y[i]
        hill.append(i)
    elif h> y[i]:
        h=y[i]
        slope.append(i)
    elif h==y[i]:
        h=y[i]
        flat.append(i)

print(str(hill[0])+"-"+str(hill[len(hill)-1])+"=hill")
print(str(len(hill)-1)+"-"+str(slope[len(slope)-1])+"=slope")
print(str(slope[len(slope)-1])+"-"+str(flat[len(flat)-1])+"=flat")



