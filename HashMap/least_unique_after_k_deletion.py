class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        hashMap = {}

        for item in arr:
            hashMap[item] = hashMap.get(item,0) + 1

        v = list(hashMap.values())

        cnt = 0

        v.sort()

        for i in range(len(v)):
            if k > v[i]:
                k-=v[i]
                v[i] = 0
            else:
                v[i] -= k
                k = 0
            if v[i] != 0:
                cnt += 1
        return cnt
        
             