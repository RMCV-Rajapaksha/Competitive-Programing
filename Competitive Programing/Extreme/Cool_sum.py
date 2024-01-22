from math import comb

list_k, n4 = map(int, input().strip().split())
m = 998244353

count = [0] * (2**list_k)

for y in range(n4 + 1):
    count[y % (2**list_k)] += comb(n4, y) % m

answer = [num % m for num in count]

print(*answer)
