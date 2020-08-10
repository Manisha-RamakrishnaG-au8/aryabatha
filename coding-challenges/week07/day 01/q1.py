class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        val_node = {}
        
        linked_list = None
        tmp = None
        
        mover = head
        counter = 0
        while mover is not None:
            node = Node(mover.val)
            mover.val = counter
            val_node[counter] = node
            if linked_list is None:
                linked_list = node
                tmp = linked_list
            else:
                tmp.next = node
                tmp = tmp.next
            mover = mover.next
            counter+=1
            
        tmp = linked_list
        while head is not None:
            rand = head.random
            if rand:
                tmp.random = val_node[rand.val]
            else:
                tmp.random = None
            head = head.next
            tmp = tmp.next
        
        return linked_list