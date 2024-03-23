class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        start = 0
        end = 31

        while start<=end:
            mid = start + (end-start)//2
            if (2**mid == n):
                return True
            if (2**mid > n):
                end = mid - 1
            else:
                start = mid + 1
        return False
            

        