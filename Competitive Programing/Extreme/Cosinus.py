t = int(input().strip())

a_values = []

for i in range(t):
    a = float(input())
    a_values.append(a)

b_values = []


for a in a_values:
    b = 0
    c = 1

    while c != 0:
        b += 1
        if (a * b) % 90 != 0:
            c = (a * b) % 90
        else:
            c = 0
            break

    b_values.append(b)

for i in b_values:
    print(i)
