class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root==None:
            return []
        parent={}
        s=[]
        s.append(root)
        Result=[]
        while len(s)>0:
            temp=s.pop()
            #print(temp.val)
            if temp.left==None and temp.right==None:
                #print(temp.val)
                result=[]
                t=temp
                result.append(t)
                while t in parent.keys():
                    result.append(parent[t])
                    t=parent[t]
                result2=""
                print(result)
                while len(result)>0:
                    if len(result)>1:    
                        result2+=str(result.pop().val)+"->"
                    else:
                        result2+=str(result.pop().val)
                #print("r2:",result2)
                Result.append(result2)       
            if temp.left!=None:
                s.append(temp.left)
                parent[temp.left]=temp
            if temp.right!=None:
                s.append(temp.right)
                parent[temp.right]=temp
        #print(parent)
        return Result