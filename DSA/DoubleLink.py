#This file demonstration of Double Linked List perform creating , adding ,removing and displaying List

# Creating Node
class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

# Creating Linked List
class DoubleLinkedList:
    def __init__(self):
        self.head = None
        
    # Insert at beg
    def Insert_at_beg(self,data):
        nb = Node(data)
        temp = self.head
        temp.prev = nb
        nb.next = temp
        self.head = nb  
        
    # Insert at end
    def Insert_at_end(self,data):
        ne = Node(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = ne
        ne.prev = temp 
         
    # Insert At pos
    def Insert_at_pos(self,pos,data):
        np = Node(data)
        temp = self.head
        for i in range(1,pos-1):
            temp = temp.next
        np.prev = temp
        np.next = temp.next
        temp.next.prev = np
        temp.next = np
     
    # Remove At beginning
    def Remove_at_beg(self):
        temp = self.head
        self.head = temp.next
        temp.next = None
        self.head.prev = None
        
    # Remove at end
    def Remove_at_end(self):
        before  = self.head
        temp = self.head.next
        while temp.next:
            temp = temp.next
            before = before.next
        before.next = None
        temp.prev = None
        
    #Remove At pos
    def Remove_at_pos(self,pos):
        before = self.head
        temp = self.head.next
        for i in range(1,pos-1):
            temp = temp.next
            before = before.next
        before.next = temp.next
        temp.next.prev = before
        temp.next = None
        temp.prev = None
               
           
    # Displaying Linked List    
    def display(self):
        if self.head is None:
            print("Empty Linked List")
        
        else:
            temp = self.head
            while temp:
                print(temp.data,"--->",end = " ")
                temp = temp.next


if __name__ == "__main__":
    l = DoubleLinkedList()
    n = Node(20)
    l.head = n
    l.Insert_at_beg(10)
    l.Insert_at_beg(15)
    l.Insert_at_end(30)
    l.Insert_at_end(40)
    l.Insert_at_end(50)
    l.Insert_at_pos(4,35)
    l.Remove_at_beg()
    #l.Remove_at_end()
    #l.Remove_at_pos(4)
    l.display()
        