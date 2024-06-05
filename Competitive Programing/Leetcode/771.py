class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        c=0
        jewels=set(jewels)
        for i in stones:
            if i in jewels:
                c+=1
        return c
    