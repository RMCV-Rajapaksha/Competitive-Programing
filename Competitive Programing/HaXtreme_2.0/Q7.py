def split_list(a_list):
    half = len(a_list) // 2
    return a_list[:half], a_list[half:]

# Input format validation
initial = input().split(".")
if len(initial) != 3:
    initial.extend(["000000"] * (3 - len(initial)))  # Extend the input with "000000" to make it three parts

x, y, z = initial

x1, x2 = split_list(x)
y1, y2 = split_list(y)
z1, z2 = split_list(z)

# Convert binary strings to decimal
numx1 = int(x1, 2)
numx2 = int(x2, 2)
numy1 = int(y1, 2)
numy2 = int(y2, 2)
numz1 = int(z1, 2)
numz2 = int(z2, 2)

result = (
    str(numx1) + str(numx2) + "-"
    + str(numy1) + str(numy2) + "-"
    + str(numz1) + str(numz2)
)
print(result)