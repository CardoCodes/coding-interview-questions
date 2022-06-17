class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]) -> int:
            if not node: return 0

            res = dfs(node.left)+dfs(node.right) 

            curr = min(node.left.val if node.left else float('inf'), node.right.val if node.right else float('inf')) #check if current node is a root node  / next node in line to monitor

            if curr == 0: # if atleast one child node requires monitoring,this node must have camera
                node.val = 1
                res += 1

            elif curr ==1: #at least one chiold node is a camera, this node is already monitored
                node.val = 2
            
            return res
        return dfs(root) + (root.val == 0)