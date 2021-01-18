class Node:
	def __init__(self,data):
		self.data = data
		self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node    		

    def get_nth(self, index):
        current = self.head
        count = 0

        while (current):
            if (count == index):
                return current.data
            count += 1
            current = current.next

        # if we get to this line the caller was asking for a non-existent element so we assert fail
        assert(False)
        return 0


if __name__ == '__main__':
	llist = LinkedList()

	llist.push(5)
	llist.push(11)
	llist.push(9)
	llist.push(23)
	llist.push(12)
	
	print("First element of the LinkedList : ",llist.get_nth(0))
	print("Fifth element of the LinkedList : ",llist.get_nth(4))
	
	