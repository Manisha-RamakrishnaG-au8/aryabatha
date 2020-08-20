class Solution:
    def hasPathSum(self, root: TreeNode, rsum: int) -> bool:
        if root == None:
            return False
        if root.val == rsum and root.left is None and root.right is None:
            return True
        return (self.hasPathSum(root.left, rsum - root.val) or self.hasPathSum(root.right, rsum - root.val))
		