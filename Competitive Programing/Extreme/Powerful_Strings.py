import math

# Function to calculate the power of a string
def calculate_power(s, substrings):
    power = 0
    for substring in substrings:
        pos = 0
        while pos < len(s):
            pos = s.find(substring, pos)
            if pos == -1:
                break
            pos += len(substring)
            power += 1
    return 2 ** power

# Function to generate all possible strings of length N and calculate their power
def generate_strings_and_calculate(N, alphabet, substrings):
    total_power = 0
    alphabet_size = len(alphabet)
    indices = [0] * N

    while True:
        s = ''.join(alphabet[i] for i in indices)
        total_power += calculate_power(s, substrings)

        # Increment the indices to generate the next string
        j = N - 1
        while j >= 0 and indices[j] == alphabet_size - 1:
            indices[j] = 0
            j -= 1
        if j < 0:
            # All combinations have been generated
            break
        indices[j] += 1

    return total_power

# Part 1: Getting inputs
N, M = map(int, input().split())
N = N % 998244353
substrings = [input() for _ in range(M)]

alphabet = "abcdefghijklmnopqrstuvwxyz"
total_power = 0


total_power = generate_strings_and_calculate(N, alphabet, substrings)

print(total_power)