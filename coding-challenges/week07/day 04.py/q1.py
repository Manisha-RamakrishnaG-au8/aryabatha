
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

def rightView(root):
    max_l=[0]
    helper(root,1,max_l)
    
def helper(root,le,max_l):
    if root==None:
        return 
    if le>max_l[0]:
        print(root.data,end=" ")
        max_l[0]=le
    helper(root.right,le+1,max_l)
    helper(root.left,le+1,max_l)