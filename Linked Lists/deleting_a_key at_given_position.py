class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # inserting a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Given a reference to the head of a list and a position, delete the node at a given position
    def deleteNode(self, position):

        # if linkedlist is empty
        if self.head == None:
            return 

        # store head node
        temp = self.head

        # if head node needs to be removed
        if position == 0:
            self.head = temp.next
            temp = None
            return 

        # Find previous node of the node to be deleted
        for i in range(position - 1):
            temp = temp.next
            if temp is None:
                break       

        # If position is more than no. of nodes
        if temp is None:
            return
        if temp.next is None:
            return

        # Node temp.next is the node to be deleted
        # store pointer to the next of the node to be deleted
        next = temp.next.next

        # Unlink the node from the linked list      
        temp.next = None
        temp.next = next

        # Utility function to print the linkedlist
    def printlist(self):
        temp = self.head
        while(temp):
            print (" %d " %(temp.data)),
            temp = temp.next



if __name__ == '__main__':
    
    llist = LinkedList()
    llist.push(12)
    llist.push(25)
    llist.push(7)
    llist.push(5)
    llist.push(29)
    llist.push(85)

    llist.printlist()

    llist.deleteNode(2)

    llist.printlist()








                                                        