# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        """
        DFS is oftes preferred if we want to visit every node. In this problem we will
        be having to traverse every node to return a complete inverse binary tree. Giving us
        a time complexity of "O(n)" where n is the number of nodes & a space complexity of "O(m)"
        where m is the height of the tree.
        """
        
        if not root: #base case, stops recursion
            return None
        
        root.right, root.left = root.left, root.right #swap nodes
        
        #basic dfs to visit each node
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
        