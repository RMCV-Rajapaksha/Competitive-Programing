#  MY TEST CODE
# class Solution:
#     def minPathSum(self, grid: List[List[int]]) -> int:
#         m=len(grid)
#         n=len(grid[0])
        
        
#         dp = [[0] * m for _ in range(n)]
        
#         for x in range(m):
#             if x==0:
#                 dp[0][x]=grid[0][x]
                
#             else:
#                 dp[0][x]=grid[0][x]+dp[0][x-1]
                
#         for y in range(1,n):
#                 dp[y][0]=grid[y][o]+dp[y-1][0]      
        
        
#         for x in range(1,m-1):
#             for y in range(1,n-1):
#                 dp[x][y]=min[(dp[x-1][y]+grid[x][y]),(dp[x][y-1]+grid[x][y])]
                
                
#         return dp[n-1][m-1]
                
                
from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
   
        dp = [[0] * n for _ in range(m)]
        
 
        dp[0][0] = grid[0][0]
       
        for x in range(1, m):
            dp[x][0] = dp[x-1][0] + grid[x][0]
        
   
        for y in range(1, n):
            dp[0][y] = dp[0][y-1] + grid[0][y]
        
      
        for x in range(1, m):
            for y in range(1, n):
                dp[x][y] = min(dp[x-1][y], dp[x][y-1]) + grid[x][y]
        
        return dp[m-1][n-1]

                
                
        
        
        