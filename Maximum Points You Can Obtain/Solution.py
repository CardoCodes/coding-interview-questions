class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        best = total = sum(cardPoints[:k]) #total is sum of array
        
        for i in range (k-1, -1, -1): #k cards
            
            total += cardPoints[i + len(cardPoints) - k] - cardPoints[i]
            
            best = max(best, total)
        return best