class Solution:

  def minimumLength(self, s: str) -> int:
    minLen = len(s)
    l = 0
    r = len(s) - 1
    if len(s) == 1:
      return 1
    while l < r:
      if s[l] == s[r]:
        char = s[l]
        while s[l] == char and l < r:
          l += 1
        while s[r] == char and l <= r:
          r -= 1
        minLen = min(minLen, r - l + 1)
      else:
        break
    return minLen


'''

class Solution:
  def minimumLength(self, s: str) -> int:
      left, right = 0, len(s) - 1

      while left < right and s[left] == s[right]:
          char = s[left]
          while left <= right and s[left] == char:
              left += 1
          while right >= left and s[right] == char:
              right -= 1

      return right - left + 1
'''
