class Node:

	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # x would be the element to search
    def search(self, x):   
        current = self.head

        while current != None:
        	if current.data == x:
        		return True

        	current = current.next
        
        return False


# Code execution

if __name__ == '__main__':
    llist = LinkedList()
    llist.push(39)
    llist.push(6)
    llist.push(22)
    llist.push(9)
    llist.push(11)
            	
    if llist.search(39):
    	print("The number is present in the LinkedList.")
    else:
        print("The number is absent from the LinkedList.")	
    
    