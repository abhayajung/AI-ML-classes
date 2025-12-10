class stack:
    def __init__(self):
        self.stack=[]
    
    def push(self,value):
        self.stack.append(value)   
    
    def is_empty(self):
        return len(self.stack)==0
    
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack.pop() 
    
    def peek(self):
        return self.stack[-1]
    
    def size(self):
        return len(self.stack)
    
#Object   #stack last in last out
my_stack=stack()
my_stack.push(34)
my_stack.push(35)
my_stack.push(78)
my_stack.push(88)

print(f"My stack: {my_stack.stack}")
print(f"Popped Element: {my_stack.pop()}")
print(f"Stack after pop: {my_stack.stack}")
print(f"Top element: {my_stack.peek()}")
print(f"Size of peek: {my_stack.size()}")


#Queue first in first out