class Node:

	def __init__(self,data):
		self.data = data
		self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printnthfromlast(self, n):
        temp = self.head
        
        length = 0

        while temp is not None:
        	temp = temp.next
        	length += 1

        if n > length:
            print("Location greater than the length of the  LinkedList.")
            return

        temp = self.head
        for i in range(0, length - n):
        	temp = temp.next
        print(temp.data)
        

# Driver code
if __name__ == '__main__':
    
    llist = LinkedList()
    llist.push(20)
    llist.push(18)
    llist.push(16)
    llist.push(14)
    llist.push(12)
    llist.printnthfromlast(6)        	


