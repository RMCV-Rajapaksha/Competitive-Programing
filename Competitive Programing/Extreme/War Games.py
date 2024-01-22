n = int(input())

def champion(man1, man2):
    l = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
    man1 = [l[card] for card in man1]
    man2 = [l[card] for card in man2]
    yyy=0
    while man1!=[] and man2!=[]:
        p=man1[yyy]
        Q=man2[yyy]
        if p<Q:
            man2.append(p)
            man2.pop(yyy)
            man1.pop(yyy)

        elif p>Q:
            man2.pop(yyy)
            man1.append(Q)
            man1.pop(yyy)
        elif p==Q:
            man1.append(p)
            man1.pop(yyy)
            man2.append(Q)
            man2.pop(yyy)
        if man1==man2:
            break
    if man1==[]:
        return'player 2'
    elif man2==[]:
        return 'player 1'
    else:
        return "draw"
ans=[]
for _ in range(0,n):
    l1=list(map(str,input().strip().split()))
    l2=list(map(str,input().strip().split()))
    print(champion(l1, l2))