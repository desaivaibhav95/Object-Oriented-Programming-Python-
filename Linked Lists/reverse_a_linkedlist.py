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

    def reverse(self):
        previous = None  # previous node as None
        current = self.head  # first node as current

        while current is not None:  # traversing until the last node of the linkedlist is reached  
            next = current.next  # next of current
            current.next = previous # assigning previous to next of current thus, first element becomes the and element and points to None
            previous = current # further assigning current as previous
            current = next # next as current

        self.head = previous # once traversed until last node set previous as the head (first node)
    
    def printlist(self):
        temp = self.head
        while (temp):
            print (temp.data),
            temp = temp.next


if __name__ == '__main__':

    ll = LinkedList()
    ll.push(1)
    ll.push(3)
    ll.push(4)
    ll.push(5)
    ll.push(6)
    ll.push(8)
    ll.push(11)
    print("Linkedlist :")
    ll.printlist()

    ll.reverse()
    print("Reversed Linkedlist :")
    ll.printlist()