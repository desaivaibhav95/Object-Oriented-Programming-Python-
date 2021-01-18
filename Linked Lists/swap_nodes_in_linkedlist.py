# swapping two given nodes of a given linkedlist without swapping data

class LinkedList(object):
    def __init__(self):
        self.head = None


    class Node(object):
        def __init__(self, d):
            self.data = d
            self.next = None

    def swapNodes(self,x,y):
        
        # Nothing to do if x and y are same
        if x == y:  
            return 

        # search for x (keeping track of previous x and current x)
        previous_X = None
        current_X = self.head
        while current_X != None and current_X.data != x:
            previous_X = current_X
            current_X = current_X.next

        # search for y (keep track of previous y and current y)
        previous_Y = None
        current_Y = self.head
        while current_Y != None and current_Y.data != y:
            previous_Y = current_Y
            current_Y = current_Y.next

        # If either x or y is not present, nothing to do
        if current_X is None or current_Y is None:
            return

        # If x is not head of linkedlist
        if previous_X != None:
            previous_X.next = current_Y
        else:
            self.head = current_Y

        # If y is not head of linkedlist
        if previous_Y != None:
            previous_Y.next = current_X
        else:
            self.head = current_X

        # Swap next pointers
        temp = current_X.next
        current_X.next = current_Y.next
        current_Y.next = temp


    # Function to add Node at the beginning of the list
    def push(self, new_data):
        new_node = self.Node(new_data)
        new_node.next = self.head
        self.head = new_node

    
    def printlist(self):
        tnode = self.head
        while tnode != None:
            print (tnode.data)
            tnode = tnode.next 


if __name__ == '__main__':
    llist = LinkedList()
    llist.push(2)                        
    llist.push(6)                        
    llist.push(12)                        
    llist.push(21)                        
    llist.push(15)                        
    llist.push(9)

    print("Linkedlist before node swapping : ")
    llist.printlist()

    llist.swapNodes(12,9)

    print("\n Linkedlist after node swapping : ")
    llist.printlist()
