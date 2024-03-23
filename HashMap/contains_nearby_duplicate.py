class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashSet = {}

        for i,num in enumerate(nums):
            if num in hashSet and i - hashSet[num] <=k:
                return True

            hashSet[num] = i
        return False


        