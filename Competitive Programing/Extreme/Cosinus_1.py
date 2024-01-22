from decimal import Decimal
from fractions import Fraction



def calculate_b_for_angles(t, angle_values):
    b_values = []

    for a in angle_values:
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

    return b_values

def config():
    t = int(input().strip())
    angle_values = []

    for i in range(t):
        a = Decimal(input())
        angle_values.append(a)

    b_values = calculate_b_for_angles(t, angle_values)

    for i in b_values:
        print(i)

if __name__ == "__main__":
    config()
