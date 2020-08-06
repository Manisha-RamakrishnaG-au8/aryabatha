class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        length = 0
        node = head
		
		#iterate over LL to obtain length
        while(node):
            length+=1
            node = node.next
        print(length)
        if length%2 == 0:
            mid = (length/2)+1
        else:
            mid = int((length/2)+0.5)
        print(mid)
		
		#iterate over LL till midpoint and return remaining LL
        length = 0
        while(head):
            length+=1
            if length == mid:
                return head
            head = head.next