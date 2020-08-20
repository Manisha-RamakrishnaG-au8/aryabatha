
class Node: 
	def __init__(self, data): 
		self.data = data 
		self.next = None


def push(head_ref, new_data): 
	new_node = Node(0) 
	new_node.data = new_data 
	new_node.next = (head_ref) 
	(head_ref) = new_node 
	return head_ref 

def deleteKey(head_ref, key): 
	
	# Store head node 
	temp = head_ref 
	prev = None

	while (temp != None and temp.data == key): 
		head_ref = temp.next # Changed head 
		temp = head_ref		 # Change Temp 
	
	# Delete occurrences other than head 
	while (temp != None): 
	
		while (temp != None and temp.data != key): 
			prev = temp 
			temp = temp.next
		
		# If key was not present in linked list 
		if (temp == None): 
			return head_ref 

		# Unlink the node from linked list 
		prev.next = temp.next

		# Update Temp for next iteration of outer loop 
		temp = prev.next
		return head_ref 

def printList(node): 
	while (node != None): 
		print(node.data,"end =" "") 
		node = node.next
	
# Driver Code 
if __name__=='__main__': 
	
	# Start with the empty list 
	head = None

	head = push(head, 7) 
	head = push(head, 2) 
	head = push(head, 3) 
	head = push(head, 2) 
	head = push(head, 8) 
	head = push(head, 1) 
	head = push(head, 2) 
	head = push(head, 2) 

	key = 2 # key to delete 

	print("Created Linked List: ") 
	printList(head) 
	
	head = deleteKey(head, key) 
	print("\n Linked List after Deletion is: ") 

	printList(head) 
