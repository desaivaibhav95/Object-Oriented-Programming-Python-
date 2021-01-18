class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def deletelist(self):
        
        current = self.head
        while current:
            previous = current.next

            del current.data

            current = previous


    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # utility function to print linkedlist
    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

if __name__ == '__main__':
    
    ll = LinkedList()
    ll.push(5) 
    ll.push(12) 
    ll.push(27) 
    ll.push(9) 
    ll.push(15) 
    
    print("LinkedList has been generated.")
    ll.printlist()

    ll.deletelist()
    print("LinkedList has been deleted.")