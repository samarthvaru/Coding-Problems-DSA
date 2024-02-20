class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        secondMax = float('-inf')

        maxV = float('-inf')
        
        for i in nums:
            if i > maxV:
                secondMax = maxV
                maxV = i
            elif i > secondMax:
                secondMax = i

        return (maxV - 1) * (secondMax -1)
        