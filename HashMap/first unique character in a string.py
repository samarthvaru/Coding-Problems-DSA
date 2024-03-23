class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict= {}
        for i in s:
            if i not in dict:
                dict[i]=1
            else:
                dict[i]+=1
        index= -1
        for i in range(len(s)):
            if dict[s[i]]== 1:
                index= i
                break     
        return index 