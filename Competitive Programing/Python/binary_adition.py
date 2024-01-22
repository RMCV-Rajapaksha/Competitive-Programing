class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result = []

        max_length = max(len(a), len(b))
        a = a.zfill(max_length)
        b = b.zfill(max_length) #zfill use to fill the binary number 

        for i in range(max_length - 1, -1, -1):
            bit_a = int(a[i])
            bit_b = int(b[i])

      
            total = bit_a + bit_b + carry

            
            result.insert(0, str(total % 2))
            carry = total // 2

        if carry:
            result.insert(0, '1')

        return ''.join(result)


solution = Solution()
a = '01010'
b = '00011'
print(solution.addBinary(a, b))  
