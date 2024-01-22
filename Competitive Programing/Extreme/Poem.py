n1,m1 = list(map(int,input().split()))

s=[]
p=[]

for _ in range(n1):
    s.append(tuple(map(str,input().split())))
input()
for _ in range(1,m1*2+1,2):
    p.append(list(map(str,input().split()))[-1])
w=[]
l=[]
for t in p:
    for u in range(n1):
        if t.lower() in s[u]:
            w.append(t)
            l.append(u)
            break
    else:
        w.append(t)
        l.append("X")
temp=-1
status=False
p=1
while p+1<m1:
    if l[p-1]=="X" and m1>2:
        if l[p]!=l[p+1]:
            l[p]="X"
            p+=1
        else:
            temp=l[p]
            while p<m1-2:
                if l[p]==temp:
                    l[p], l[p+1]="X"*2
                    p+=2
                p+=1
    p=p+1
l=[x for x in l if x!="X"]
d=list(dict.fromkeys(l))
alph=("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","Y","Z")
letters={k:l for (k,l) in zip(d,alph[0:len(d)])}
i=0
while  i<m1:
    if l[i]!="X":
        l[i]=letters[l[i]]
    i+=1

print(''.join(l))