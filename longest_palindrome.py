class Solution:
    def longestPalindrome(self, s: str) -> int:
        odd_count = 0
        hashmap = {}
        
        for ch in s:
            if ch in hashmap:
                hashmap[ch] +=1
            else:
                hashmap[ch] = 1
            if hashmap[ch]%2 == 1:
                odd_count += 1
            else:
                odd_count -=1
        
        if odd_count > 1:
            return len(s) - odd_count + 1
        return len(s)