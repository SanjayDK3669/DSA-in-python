# This is Demonstration of Linked List

# Creating Node
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

# Creating Linked List

class LinkedList:
    def __init__(self):
        self.head = None
        
    # Insert at the beginning
    def Insert_beg(self,data):
        nb = Node(data)
        nb.next = self.head
        self.head = nb
        
    # Insert at the end
    def Insert_end(self,data):
        ne = Node(data)
        temp  = self.head
        while temp.next:
            temp  = temp.next
        temp.next = ne
        
    # Insert at the position
    def Insert_pos(self,index,data):
        np = Node(data)
        temp = self.head
        for i in range(index-1):
            temp = temp.next
        np.data = data
        np.next = temp.next
        temp.next = np
        
    # Remove at beg
    def Remove_at_beg(self):
        temp = self.head
        self.head = temp.next
        temp.next = None
        
    #Remove at end
    def Remove_at_end(self):
        before = self.head
        temp = self.head.next
        while temp.next:
            temp = temp.next
            before = before.next
        before.next = None
    
    # Remove at position
    def Remove_at_pos(self,pos):
        before = self.head
        temp = self.head.next
        for i in range(1,pos-1):
            temp = temp.next
            before = before.next 
        before.next = temp.next   
            
    
        
    # Display the list
    def display(self):
        if self.head is None:
            print("Linked list is empty")
        
        else:
            temp = self.head
            while temp:
                print(temp.data,"--->",end = " ")
                temp = temp.next


l = LinkedList()
n = Node(10)
l.head = n
n1 = Node(20)
n.next = n1
n2 = Node(30)
n1.next = n2
l.Insert_beg(1)
l.Insert_beg(5)
l.Insert_end(50)
l.Insert_end(60)
l.Insert_pos(3,25)
l.Insert_pos(8,45)
#l.Remove_at_beg(4)
#l.Remove_at_end()
#l.Remove_at_pos(5)
l.display()

