class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            # if newInterval end is less than current interval start
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # if newinterval start is greater than current interval end
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            
            # overlap, so fix
            else:
                newInterval = [
                    min(intervals[i][0],newInterval[0]),
                    max(intervals[i][1],newInterval[1])
                ]
        res.append(newInterval)
        return res

