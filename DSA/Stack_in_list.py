# STACK
# A new element is added at one end and an element is removed from that end only
# Insert  = push, Delete = pop 
# Implemented using the list, Collections.deque, queue.LifoQueue

#Stack Implementation using list 
# Pushing the elements
def push():
    n1 = int(input("Enter Insert Element: "))
    if len(stack)==0:
        stack.append(n1)
    else :
        stack.insert(0,n1)
        print(n1," is inserted into stack")

#Popping the  elements       
def pop():
    if len(stack) ==0:
        print("Stack is Empty")
    else:
        print(stack[0]," is deleted")
        del stack[0]

#Display the elements
def display():
    if len(stack) == 0:
        print("stack is Empty")
    else:
        print("Elements of stack are: ")
        for ele in stack:
            print(ele)
        print("Top of the stack:",stack[0])
        
        
stack = list()
print(" 1 --> Push\n 2 --> Pop \n 3 --> Display\n Any -->Exit")
try:
    while(True):
        n = int(input("Enter your choice: "))
        if n == 1:
            print("Push")
            push()
        elif n == 2:
            print("Pop")
            pop()
        elif n == 3:
            print("Display")
            display()
        else:
            print("Exit")
            break
except Exception  :
    print("Please enter any number")


    
