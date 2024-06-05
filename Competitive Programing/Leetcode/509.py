class Solution:
    @__cached__
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        return self.fib(n - 1) + self.fib(n - 2)
    



# class Solution:
#     def fib(self, n: int) -> int:
#         if n <= 1:
#             return n

#         memo = {0: 0, 1: 1}
#         for i in range(2, n + 1):
#             memo[i] = memo[i - 1] + memo[i - 2]

#         return memo[n]
