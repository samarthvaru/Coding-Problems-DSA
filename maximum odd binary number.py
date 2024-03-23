class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count_1 = Counter(s).get('1')
        new_s = ""
        for i in range(len(s)-1):
            if count_1 - 1 > 0:
                new_s += "1"
                count_1 -= 1
            else:
                new_s += "0"
        
        new_s += "1"

        return new_s
