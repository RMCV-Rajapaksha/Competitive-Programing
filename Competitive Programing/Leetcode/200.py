from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        m = len(grid)
        n = len(grid[0])
        count = 0
        max_area = 0

        def DFS(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != '1':
                return 0
            grid[i][j] = '0'
            return 1 + DFS(i, j + 1) + DFS(i + 1, j) + DFS(i - 1, j) + DFS(i, j - 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    max_area = max(max_area, DFS(i, j))

        return count
