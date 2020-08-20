class Solution(object):
    def searchBST(self, root, val):
        # iterative solution 
        stack = []
        stack.append(root)
        
        while stack:
            node = stack.pop()            
            if node.val == val:                 #if it is equal return value
                return node            
            elif node.val > val:                # if current node is greater than target value, look left side of the tree
                if node.left:
                    stack.append(node.left)
            else:                               # if current node is less than target value, look right side of the tree
                if node.right:
                    stack.append(node.right)
        return None     
    
        # recursive solution               
        if not root:                                # base case
            return
        if root.val == val:                         #if it is equal return value
            return root
        elif root.val > val:
            return self.searchBST(root.left,val)    # if current node is greater than target value, look left side of the tree
        else:
            return self.searchBST(root.right,val)   # if current node is less than target value, look right side of the tree

    