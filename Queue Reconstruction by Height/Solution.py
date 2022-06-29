class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        #print('initial array: ',people)
        
        people.sort(key = lambda x: (-x[0], x[1])) #sort by height first, then by k
        arr = []
    
        #greedy algo, insert the entry in the output array based on k val
        #k will at as a position within the array
        for p in people:
            arr.insert(p[1], p)
        
        #print('sorted array: ', people)
        #print('answer: ', arr)
        return arr