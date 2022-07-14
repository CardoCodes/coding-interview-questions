class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return
        
        Root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        Root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        Root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        
        return Root