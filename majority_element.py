## solution 1 : hashmap T: 0(n) space: 0(n)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        res, maxCount = 0,0
        
        for n in nums:
            count[n] = 1+count.get(n,0)
            res = n if count[n] > maxCount else res
            maxCount = max(maxCount,count[n])
        return res 
    
## solution 2 :  T: 0(n) space: 0(1)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        res,count = 0,0

        for n in nums:
            if count == 0:
                res = n
            count += 1 if res==n else -1
        return res