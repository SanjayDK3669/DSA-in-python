#Deque :- Double ended Queue
from collections import deque
class Stack:
    def __init__(self):
        self.container = deque()
        
    def push(self,data):
        self.container.append(data)
    
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]
    
    def is_return(self):
        return len(self.container)
    
    def size(self):
        return len(self.container)
    
print("1 --> push\n 2 --> pop\n 3 -->peek\n 4 -->size\n 5 -->exit")
s = Stack()
while True:
    n = int(input("Enter your  choice: "))
    if n == 1:
        data =input("Enter the pushing data: ")
        print("Push")
        s.push(data)
    elif n == 2:
        print("Pop",s.pop())
        
    elif n == 3:
        print("Peek",s.peek())
        
    elif n == 4:
        print("Size",s.size())
        
    else:
        print("Exit")
        break

    
        
#stack = deque()
