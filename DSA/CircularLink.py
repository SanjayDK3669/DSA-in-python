# Creating Circular Linked list  and perform the insertion and deletion process

#Create Node
class Node:
    def __init__(self,data):
        self.data = data
        self.next  = None
        
class Circular_List:
    def __init__(self):
        self.head = None
        self.tail  = None
        
    # insertion at beginning
    def Insert_at_beg(self,data):
        nb = Node(data)
        if self.head is None:
            self.head = nb
            self.tail = nb
            self.tail.next = nb
            
        else:
            nb.next = self.head
            self.tail.next = nb
            self.head = nb
            
        #Insertion At end
    def Insert_at_end(self,data):
        ne = Node(data)
        if self.head is None:
            self.head = ne
            self.tail = ne
            self.tail.next = self.head
        else:
            self.tail.next = ne
            self.tail = ne
            self.tail.next = self.head
    
    # Insertion at position
    def Insert_at_pos(self,pos,data):
        np = Node(data)
        if self.head is None:
            self.head = np
            self.tail = np
            self.tail.next = self.head    
        else:
            if pos == 1:
                l.Insert_at_beg(data)
            else:
                temp = self.head
                for i in range(1,pos-1):
                    temp = temp.next 
                np.next = temp.next
                temp.next = np 
    # get the length of list
    def Get_len(self):
        temp = self.head
        count = 1
        while temp != self.tail:
            temp = temp.next
            count += 1
        return count
        #print(count)    
                
    # Remove at beg
    def Remove_at_beg(self):
        if self.head is None:
            print("Empty List")
        else:
            if self.head == self.tail:
                self.head = None
            else:
                temp = self.head
                self.head = temp.next
                self.tail.next = self.head
                temp = None 
    # Remove at end
    def Remove_at_end(self):
        if self.head is None:
            print("Empty list")
        else:
            if self.head == self.tail:
                self.head = None
            else:
                temp = self.head
                while temp.next != self.tail:
                    temp = temp.next
                self.tail = None
                self.tail = temp
                self.tail.next = self.head
    # Remove at pos
    def Remove_at_pos(self,pos):
        if pos > 0 and pos <= int(l.Get_len()):
            if self.head is None:
                print("Empty List")
            elif pos == 1:
                l.Remove_at_beg()
            else:
                before = self.head
                temp = self.head.next
                for i in range(1,pos-1):
                    before = before.next
                    temp = temp.next
                before.next  = temp.next
                if temp == self.tail:
                    self.tail = before
                temp = None
        else :
            print("Invalid position")               
            
    #Display the list
    def display(self):
        if self.head is None:
            print("Empty List")
        else:
            temp = self.head
            print(temp.data,"-->",end = " ")
            while temp.next != self.head:
                temp = temp.next
                print(temp.data,"-->",end = " ")
                
            print(temp.next.data)
if __name__ == "__main__":
    l = Circular_List()
    n = Node(10)
    l.head = n
    l.tail = n
    l.tail.next = l.head
    l.Insert_at_beg(5)
    l.Insert_at_beg(2)
    l.Insert_at_end(20)
    l.Insert_at_end(30)
    l.Insert_at_pos(4,50)
    l.Insert_at_pos(4,60)
    l.Insert_at_beg(80)
    l.Get_len()
    #l.Remove_at_beg()
    #l.Remove_at_end()
    #l.Remove_at_pos(4)
    l.Remove_at_pos(5)
    l.display()