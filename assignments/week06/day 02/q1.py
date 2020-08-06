class Node:
    
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None
    
    
class MyLinkedList:

    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
        

    def get(self, index: int) -> int:
        if index >= self.size:
                return -1
        
        if index > self.size/2:
            pointer = self.tail
            countdown = self.size
            while countdown != index:
                pointer = pointer.prev
                countdown -= 1
            return pointer.val
        else:
            pointer = self.head
        
            if index == 0:
                return pointer.next.val

            for i in range(index+1):
                pointer = pointer.next
            return pointer.val

    
    def addAtHead(self, val: int) -> None:
        pointer = self.head
        
        new_node = Node(val)
        new_node.next = pointer.next
        new_node.prev = pointer
        pointer.next.prev = new_node
        pointer.next = new_node
        self.size += 1
        
        return self.head

    
    def addAtTail(self, val: int) -> None:
        pointer = self.tail
        
        new_node = Node(val)
        new_node.next = pointer
        new_node.prev = pointer.prev
        pointer.prev.next = new_node
        pointer.prev = new_node
        self.size += 1
        
        return self.tail
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        elif index > self.size:
            return self.head
        else:
            new_node = Node(val)
            
            if index > self.size/2:
                pointer = self.tail
                countdown = self.size
                while countdown != index:
                    pointer = pointer.prev
                    countdown -= 1
                new_node.next = pointer
                new_node.prev = pointer.prev
                pointer.prev.next = new_node
                pointer.prev = new_node
                self.size += 1
                
                return self.tail
            else:
                pointer = self.head
                for i in range(index+1):
                    pointer = pointer.next
                new_node.next = pointer
                new_node.prev = pointer.prev
                pointer.prev.next = new_node
                pointer.prev = new_node
                self.size += 1
                
                return self.head

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return self.head
        
        if index > self.size/2:
            pointer = self.tail
            countdown = self.size
                
            while countdown != index:
                pointer = pointer.prev
                countdown -= 1
            pointer.prev.next = pointer.next
            pointer.next.prev = pointer.prev
            pointer.next = None
            pointer.prev = None
            self.size -= 1
                
            return self.tail
        else:
            pointer = self.head
            for i in range(index+1):
                pointer = pointer.next
                
            pointer.prev.next = pointer.next
            pointer.next.prev = pointer.prev
            pointer.next = None
            pointer.prev = None
            self.size -= 1
                
            return self.head