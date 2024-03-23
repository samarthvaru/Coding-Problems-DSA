class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l,r = 0, len(nums) - 1

        def findFirst(l,r):
            while l<=r:
                mid = l + (r-l)//2
                if nums[mid] >= target:
                    r = mid - 1
                else:
                    l = mid + 1
            return l
        
        def findLast(l,r):
            while l<=r:
                mid = l + (r-l)//2
                if nums[mid] <= target:
                    l = mid+1
                else:
                    r = mid - 1
            return r
        
        first = findFirst(l,r)
        last = findLast(l,r)

        if first > r or first < 0 or nums[first] != target:
            return [-1,-1]
        return [first,last]

        