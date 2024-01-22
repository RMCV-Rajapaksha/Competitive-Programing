
n, m = map(int, input().split())

rhyming = {} 

for i in range(n):
    w = input().split()
    for w1 in w:
        rhyming[w1.lower()] = chr(65 + i % 25)  

input()  


p = [line.lower().split() for _ in range(m)]
r = []

for line in p:
    l = set() 
    for word in line:
        label = rhyming.get(word, 'X')  
        l.add(label)
    if len(l) == 0:
        r.append('X')
    else:
        r.append(''.join(sorted(l)))

print(''.join(r))
