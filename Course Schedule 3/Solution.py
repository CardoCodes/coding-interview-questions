class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        # courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]
        # SRT FIN
        # 100 200 Count = 100 < 200
        # 200 300 Count = 300 < 300
        # 1000 1250 Count = 1300 !< 1250 DOESNT WORK (1 -> 2 -> 3)
        
        # SRT FIN
        # 100 200 Count = 100 < 200
        # 1000 1250 Count = 1100 < 1250
        # 200 1300 Count = 1300 <= 1300 WORKS (1 -> 3 -> 2)
        
        heap, total = [], 0 #keep track of variables
        
        for duration, lastday, in sorted(courses, key = lambda el: el[1] ):
            if duration + total <= lastday:
                total += duration
                heappush(heap, -duration)
            elif heap and -heap[0] > duration:
                total += duration + heappop(heap)
                heappush(heap, -duration)
        return len(heap)