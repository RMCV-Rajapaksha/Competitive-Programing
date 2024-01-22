from collections import Counter,OrderedDict

n = int(input().strip())


for _ in range(n):
    lower="abcdefghijklmnopqrstuvwxyz"
    data="ABCDEFG"
    line=list(input())
    line=[x for x in line if x in lower]
    res=Counter(line).most_common()
    for i in res:
        if i[0].upper() in data:
            print(i[0].upper())
            break