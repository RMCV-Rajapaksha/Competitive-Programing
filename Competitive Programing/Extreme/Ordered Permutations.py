MOD = 10**9 + 7

def count_permutations(N, restrictions):
    dp = [0] * (N + 1)
    dp[0] = 1

    for i in range(1, N + 1):
        for r in restrictions:
            if r == '<':
                dp[i] += dp[i - 1]
            else:
                dp[i] += sum(dp[:i])
            dp[i] %= MOD

    return dp[N]

N = int(input())
restrictions = input().strip()

result = count_permutations(N, restrictions)
print(result)
