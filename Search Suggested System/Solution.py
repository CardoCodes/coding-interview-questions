class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        op = []
        
        for i in range(0, len(searchWord)):
            x = searchWord[:i+1]
            searched_result = []
            for y in products:
                if y.startswith(x):
                    searched_result.append(y)
                
                searched_result.sort()
                searched_result = searched_result[:3]
            
            op.append(searched_result)
        
        return op