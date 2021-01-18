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

    def print_middle(self):
        slow_ptr = self.head  # slow pointer object initiated at the first node (head)
        fast_ptr = self.head  # fast pointer object initiated at the first node (head)

        if (self.head != None):  # if head exists 
            while fast_ptr != None and fast_ptr.next != None:  # if the element fast pointer and its next element exists
                fast_ptr = fast_ptr.next.next # move fast pointer by two places
                slow_ptr = slow_ptr.next # move slow pointer by one place
    # The above while loop runs until the fast_ptr.next is None i.e. the Linkedlist comes to an end and the fast_ptr points to the last element of the 
    # linkedlist by completing a complete traversal and the slow pointer points to the middle element by traversing through half the linkedlist.
            print("The middle element is",slow_ptr.data)            
            


if __name__ == '__main__':
    
    ll = LinkedList()
    ll.push(1)
    ll.push(3)
    ll.push(5)
    ll.push(7)
    ll.push(9)
    ll.push(11)
    ll.push(13)
    ll.push(15)
    ll.push(17)
              
    ll.print_middle()            		