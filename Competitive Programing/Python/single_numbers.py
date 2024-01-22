
def singleNumber(nums):
        for i in nums:
            y=nums.count(i)
            if y==1:
                print (i)
            
singleNumber([6,7,3,7,6,4,3,3,3,6,8])