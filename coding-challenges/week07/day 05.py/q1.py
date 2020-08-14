class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
      if not root:
        return []
      a = root
      l = [[root.val]]
      d = [a.left, a.right]
      while d:
        temp = []
        ll = []
        for i in d:
          if not i:
            continue
          ll += [i.val]
          temp += [i.left, i.right]
        else:
          if ll:
            l += [ll]
          d = temp
      return l