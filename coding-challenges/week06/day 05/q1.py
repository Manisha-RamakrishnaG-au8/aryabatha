class MinStack:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l=[]
        
    def push(self, x: int) -> None:
        a=self.getMin()
        if a==None or x<a:
            a=x
        self.l.append((x,a))
       #self.a=self.getMin()
    def pop(self) -> None:
        self.l.pop()
    def top(self) -> int:
        if len(self.l)==0:
            return None
        else:
            return self.l[-1][0]

    def getMin(self) -> int:
        if len(self.l)==0:
            return None
        else:
            return self.l[-1][1]