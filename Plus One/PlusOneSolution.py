from typing import List

class Solution:
    def plusOne( digits: List[int]) -> List[int]:

        #transfrom array of integers into string of integers
        str1 = ""
        for i in digits:
            str1 += str(i)

        # covert str1 into integer
        int1 = int(str1) + 1
        str1 = str(int1)

        l = []

        for i in str1:
            l.append(int(i))

        print(l)
        return l

Solution.plusOne([1,2,3,4,5])        
        
        
    