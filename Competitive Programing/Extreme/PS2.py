def parser():
    while True:
        data = input().split()
        for number in data:
            if len(number) > 0:
                yield number

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)

N, M = get_number(), get_number()
S = []

for _ in range(M):
    S.append(get_word())

MOD = 998244353

def calculate_power(N, M, S):
    dp = [0] * (N + 1)
    dp[0] = 1
    
    for i in range(1, N + 1):
        for j in range(M):
            s_len = len(S[j])
            if i >= s_len:
                dp[i] = (dp[i] + dp[i - s_len]) % MOD
    
    total_power = 0
    for i in range(1, N + 1):
        total_power = (total_power + (2 ** i) * dp[i]) % MOD
    
    return total_power

result = calculate_power(N, M, S)
print(result)
