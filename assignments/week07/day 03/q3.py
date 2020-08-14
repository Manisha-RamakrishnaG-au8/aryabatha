class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
      if not root:
        return []
      def recur(node, p):
        p += [node.val]
        if node.left:
          recur(node.left, p)
        if node.right:
          recur(node.right, p)
        return p
      return recur(root, [])