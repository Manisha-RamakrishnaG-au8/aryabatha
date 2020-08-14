class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        output = []
        stack =[root]
        
        if not root:
            return None
        
        # iterate only when there is elements inside the stack.
        while stack:
            
            # pop the element from stack and stored it into temp
            temp=stack.pop()
            
            #append the value of temp to output
            output.append(temp.val)
            
            #Now traverse through left node and add the node to stack
            if temp.left:
                stack.append(temp.left)
                
            #else traverse through right node and add to stack
            if temp.right:
                stack.append(temp.right)
         
        # After iterating through the stack,  print the result in reverse order.  
        return output[::-1]