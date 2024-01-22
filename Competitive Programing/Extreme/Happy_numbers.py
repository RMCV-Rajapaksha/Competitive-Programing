def is_happy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        next_n = 0
        while n > 0:
            digit = n % 10
            next_n += digit * digit
            n //= 10
        n = next_n
    return n == 1

def count_happy_numbers(a, b):
    count = 0
    for n in range(a, b + 1):
        if is_happy(n):
            count += 1
    return count

a, b = map(int, input().split())
print(count_happy_numbers(a, b))
