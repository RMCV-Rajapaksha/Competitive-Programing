def champion(man1, man2):
    card_values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
    
    man1 = [card_values[card] for card in man1]
    man2 = [card_values[card] for card in man2]

    while man1 and man2:
        p = man1[0]
        Q = man2[0]

        if p < Q:
            man2.append(p)
            man2.pop(0)
            man1.pop(0)
        elif p > Q:
            man2.pop(0)
            man1.append(Q)
            man1.pop(0)
        else:
            man1.append(p)
            man1.pop(0)
            man2.append(Q)
            man2.pop(0)

    if not man1:
        return 'player 2'
    elif not man2:
        return 'player 1'
    else:
        return "draw"

n = int(input())
ans = []

for _ in range(n):
    l1 = input().strip().split()
    l2 = input().strip().split()
    ans.append(champion(l1, l2))

for result in ans:
    print(result)
