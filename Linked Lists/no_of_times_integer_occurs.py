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

    # counts the no. of occurences of a node in a linkedlist
    def count(self, search_for):
        current = self.head
        count = 0
        while (current is not None):  # traversing through the linkedlist
            if current.data == search_for:  # if the data of the node is what we are looking for
                count += 1  # increment the counter

            current = current.next
        return count   

    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next     


# code execution
if __name__ == '__main__':
    
    ll = LinkedList()
    ll.push(4)
    ll.push(1)
    ll.push(3)
    ll.push(1)
    ll.push(1)
    ll.push(9)
    ll.push(1)
    ll.push(12)
    
    ll.printlist()
    
    print("Number of times '1' occurs is",ll.count(1))