from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        #sorting the lists in the list by the first element
        intervals.sort(key = lambda x: x[0])
        n = len(intervals)
        
        res = [intervals[0]]

        #loop through the length of intervals to compare
        for i in range(1, n):
            #compare position of first value of interval[i] to the last value of res, if LTE then append new values
            if intervals[i][0] <= res[-1][1]:

                #placeholder for new values
                a, b = res[-1][0], res[-1][1]

                #pop old array
                res.pop()

                #append res with new array values
                res.append([a, max(b, intervals[i][1])])
            else:
                res.append(intervals[i])
        return res