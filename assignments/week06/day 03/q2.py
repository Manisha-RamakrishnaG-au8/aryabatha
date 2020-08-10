
# Node class 
class Node: 
	# Function to initialise the node object 
	def __init__(self, data): 
		self.data = data # Assign data 
		self.next = None # Initialize next as null 

class LinkedList: 

	# Function to initialize head 
	def __init__(self): 
		self.head = None


	def push(self, new_data): 

		# 1 & 2: Allocate the Node & 
		#	 Put in the data 
		new_node = Node(new_data) 

		# 3. Make next of new Node as head 
		new_node.next = self.head 

		# 4. Move the head to point to new Node 
		self.head = new_node 

	def getCount(self): 
		temp = self.head # Initialise temp 
		count = 0 # Initialise count 
        		while (temp): 
			count += 1
			temp = temp.next
		return count 


# Code execution starts here 
if __name__=='__main__': 
	llist = LinkedList() 
	llist.push(1) 
	llist.push(3) 
	llist.push(1) 
	llist.push(2) 
	llist.push(1) 
	print ("Count of nodes is :",llist.getCount()) 

# Node class 
class Node: 

	# Constructor to initialize the node object 
	def __init__(self, data): 
		self.data = data 
		self.next = None

class LinkedList: 

	# Function to initialize head 
	def __init__(self): 
		self.head = None

	def reverse(self, head, k): 
		current = head 
		next = None
		prev = None
		count = 0
		
		# Reverse first k nodes of the linked list 
		while(current is not None and count < k): 
			next = current.next
			current.next = prev 
			prev = current 
			current = next
			count += 1


		if next is not None: 
			head.next = self.reverse(next, k) 

		# prev is new head of the input list 
		return prev 

	# Function to insert a new node at the beginning 
	def push(self, new_data): 
		new_node = Node(new_data) 
		new_node.next = self.head 
		self.head = new_node 

	# Utility function to print the linked LinkedList 
	def printList(self): 
		temp = self.head 
		while(temp): 
			print temp.data, 
			temp = temp.next


# Driver program 
llist = LinkedList() 
llist.push(9) 
llist.push(8) 
llist.push(7) 
llist.push(6) 
llist.push(5) 
llist.push(4) 
llist.push(3) 
llist.push(2) 
llist.push(1) 

print "Given linked list"
llist.printList() 
llist.head = llist.reverse(llist.head, 3) 

print "\nReversed Linked list"
llist.printList() 

 
