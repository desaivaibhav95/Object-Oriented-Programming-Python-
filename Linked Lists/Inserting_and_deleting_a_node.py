# Adding a node at the front of a linkedlist
# Let's call a function push which adds an element at the front of the list. The push must receive a pointer to the head pointer,
# because push must change the head pointer to point to the new node.

class Node:
    def __init__(self, data):     # initializing the node object
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):     # initializing the first node(head)
        self.head = None
        
    def printlist(self):   # function for printing linkedlist from head(traversing through a linkedlist) 
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
            
    def push(self, new_data): # function to insert an element at the beginning of a linkedlist
        # allocate the node and load the new data
        new_node = Node(new_data) 
        # assign the current head as the next of the new node
        new_node.next = self.head 
        # finally assign new node as the new head of the linked list
        self.head = new_node
   # Time complexity of push is O(1) since it does constant amount of work


    def insert_after(self,previous_node,new_data):  # inserting a node after a specific node
        # check if the given previous node exists
        if previous_node is None:
            print("The previous node must be in Linkedlist")
            return
                
        # create a new node and put in the data
        new_node = Node(new_data)
        
        # make next of the current previous node as next of the new node
        new_node.next = previous_node.next
        
        # make new node as next of previous node
        previous_node.next = new_node

        
    def append(self,new_data):  # inserting a node at the end of a linkedlist
        # create a new node, insert in the data, set next as None
        new_node = Node(new_data) 
        
        # if the linkedlist is empty, then make the new node as head
        if self.head is None:
            self.head = new_node
            return
            
        # else traverse till the last node
        last = self.head
        while (last.next):
            last = last.next
            
        # change the next of last node
        last.next = new_node
        
     # Time complexity of append is O(n) where n is the number of nodes in the Linkedlist.
    
    
    # Deleting a Node (at a given key)
    def deleteNode(self,key):  # Given a reference to the head of a list and a key, delete the first occurence of a key in 
                                   # a linkedlist  
        # Store head node
        temp = self.head
        
        # if the head node itself holds the key to be deleted
        while (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return
            
       # Search for the key to be deleted keep track of the previous node as we need to change 'previous.next'
        while (temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
            
       # if the key was not present in the linkedlist
        if (temp == None):
            return 


#if __name__ == '__main__':

llist = LinkedList()
llist.push(8)
llist.push(12)
llist.push(4)
llist.push(23)
llist.push(6)
#print ("Created Linkedlist : ")
#llist.printlist()
llist.deleteNode(23)
llist.deleteNode(12)
print("Linkedlist after deleting two digit numbers : ")
llist.printlist()
