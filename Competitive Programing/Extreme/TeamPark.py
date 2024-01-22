def max_tickets(t, testcases):
    for _ in range(t):
        n, d, costs = testcases[_]

        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j:
                    dp[i][j] = float('inf')

        for _ in range(n * (n - 1)):
            ride_i1, ride_i2, ti = costs[_]
            dp[ride_i1 - 1][ride_i2 - 1] = min(dp[ride_i1 - 1][ride_i2 - 1], ti)

   
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

      
        max_tickets_sequence = [[0] * n for _ in range(d)]

      
        for i in range(d):
            ride_sequence = list(map(int, input().split()))
            max_tickets_sequence[i][ride_sequence[0] - 1] = 1

        for i in range(d):
            for j in range(1, n):
                for k in range(n):
                    ride_j = ride_sequence[j] - 1
                    max_tickets_sequence[i][ride_j] = max(max_tickets_sequence[i][ride_j], max_tickets_sequence[i][k] + dp[k][ride_j])

        
        for i in range(d):
            print(max(max_tickets_sequence[i]))


t = int(input())
testcases = []

for _ in range(t):
    n, d = map(int, input().split())
    costs = [list(map(int, input().split())) for _ in range(n * (n - 1))]
    testcases.append((n, d, costs))


max_tickets(t, testcases)