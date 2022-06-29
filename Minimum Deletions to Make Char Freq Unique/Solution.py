class Solution:
    def minDeletions(self, s: str) -> int:
        
        frequencies = sorted(Counter(s).values(), reverse=True) # frequency of each char in reverse order -> abbcccddd
        
        delete = 0
        next_freq = len(s)
        
        for frequency in frequencies:
            
            next_freq = min(next_freq, frequency)
            delete += frequency - next_freq
            
            if next_freq > 0:
                next_freq -=1
        
        return delete
            