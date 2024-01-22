MOD = 998244353

n, k = map(int, input().split())

def calculate_probability(n, k):
    dp = [[0] * (n + 1) for _ in range(k + 1)]

    for i in range(1, 7):
        if i <= n:
            dp[1][i] = 1

   
    for i in range(2, k + 1):
        for j in range(1, n + 1):
            for x in range(1, 7):
                if j - x >= 0:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - x]) % MOD

    
    numerator = dp[k][n]
    denominator = pow(6, k, MOD)

   
    def mod_inv(a, mod):
        return pow(a, -1, mod)

    denominator_inv = mod_inv(denominator, MOD)

    result = (numerator * denominator_inv) % MOD

    return result


t=calculate_probability(n,k)
print(t)