from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        num_row = len(matrix)
        num_column = len(matrix[0])
        num_item = num_row * num_column

        l = 0
        r = num_item - 1

        while l <= r:
            mid = (l + r) // 2
            i = mid // num_column
            j = mid % num_column

            mid_num = matrix[i][j]
            if target == mid_num:
                return True
            elif target < mid_num:
                r = mid - 1
            else:
                l = mid + 1

        return False
