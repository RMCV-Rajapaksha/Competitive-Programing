
a, b = 1, 2
even_sum = 0

while b <= 4000000:
    if b % 2 == 0:
        even_sum += b
    a, b = b, a + b

print(even_sum)
