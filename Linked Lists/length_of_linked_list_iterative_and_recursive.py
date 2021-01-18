class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
                                                                                                                                                                                                        
    def __init__(self):
        self.head = None

    def push(self,new_data):
        new_node = Node(new_data)                                                                                                                                                    
        new_node.next = self.head
        self.head = new_node

    # counting number of nodes in linkedlist iteratively, given 'node' as starting node
    def getCount(self):
        temp = self.head
        count = 0

        while (temp):
            count += 1
            temp = temp.next
        return count
        
    # code execution starts here
if __name__ == '__main__':
    llist = LinkedList()
    llist.push(1)
    llist.push(2)
    llist.push(4)
    llist.push(10)
    llist.push(21)
    print("Node count is :", llist.getCount())