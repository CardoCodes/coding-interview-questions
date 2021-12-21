class Solution(object):
    def isPowerOfTwo(self, n):
        #check to see if n is all 00000 in binary
        if n == 0:
            return False
        
        #return binary representation for twos compliment (0100 & 0100 = 0100) true
        #example of something that would not work ( 0101 & 1011 = 0111) false
        return (n & (n-1)) == 0