from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []

        ans = []
        
        letter_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def backtrack(sol, i=0):
            if i == len(digits):
                ans.append(sol)
                return
            for char in letter_map[digits[i]]:
                backtrack(sol + char, i + 1)

        backtrack('')
        return ans
