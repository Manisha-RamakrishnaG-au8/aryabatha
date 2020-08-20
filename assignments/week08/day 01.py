class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        
        #Base case:
        if root == None:
            return root
        res = []
        
        #If you traverse BST inorder, you will get the values in ascending order. Hence, you can return the (k-1)th value
        def inorder(node):
            
            if node.left:
                inorder(node.left)
            
            res.append(node.val)
    
            if node.right:
                inorder(node.right)
        
        inorder(root)
        return(res[k-1])