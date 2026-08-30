class Solution:
    def isValidBST(self, root: Optional[TreeNode], min_val = float('-inf'), max_val = float('inf')) -> bool:
        if root is None:
            return True
            
        if not (min_val < root.val < max_val):
            return False
            
        if root.left: 
            a = root.left.val 
        else: 
            a = float('-inf')
            
        if root.right: 
            b = root.right.val 
        else: 
            b = float('inf')
            
        if a < root.val < b: 
            return (self.isValidBST(root.left, min_val, root.val) and 
                    self.isValidBST(root.right, root.val, max_val) and 
                    (root.left.val < root.val if root.left else True) and 
                    (root.right.val > root.val if root.right else True))
        else: 
            return False