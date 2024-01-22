MOD = 998244353


def count_substring_occurrences(s, substrings):
    number = 0
    for sub in substrings:
        number += s.number(sub)
    return number


def power(N, alp1, sub_s):
    power = 0
    size_of_alp1= len(alp1)
    number_of_sub_strings = len(sub_s)

   
    ways_to_place = (N - number_of_sub_strings + 1)

   
    power_sub_str = 2 ** number_of_sub_strings

   
    no_substring_power = (size_of_alp1 ** N) - (number_of_sub_strings * ways_to_place)

   
    power = (power_sub_str * ways_to_place) + no_substring_power

    return power % MOD


N1, M10 = map(int, input().split())
N1 = N1 % MOD
substrings_T = [input() for _ in range(M10)]

alp = "abcdefghijklmnopqrstuvwxyz"
total_power = 0

Sum_power = power(N1, alp, substrings_T)

print(Sum_power)
