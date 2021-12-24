class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda x: x[0])
        n = len(intervals)
        
        res = [intervals[0]]
        for i in range(1, n):
            if intervals[i][0] <= res[-1][1]:
                a, b = res[-1][0], res[-1][1]
                res.pop()
                res.append([a, max(b, intervals[i][1])])
            else:
                res.append(intervals[i])
        return res