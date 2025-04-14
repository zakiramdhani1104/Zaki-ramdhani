class Stack:
 def __init__(self):
    self.items = []

 def push(self, item):
    self.items.append(item)
 
 def pop(self):
    if not self.is_empty():
        return self.items.pop()
    return None

 def peek(self):
    if not self.is_empty():
        return self.items[-1]
    return None

 def is_empty(self):
    return len(self.items) == 0

 def size(self):
    return len(self.items)

# Pengujian
stack = Stack()
stack.push("A")
stack.push("B")
stack.push("C")
stack.push("D")
print("Pop:", stack.pop()) # Output: D
print("Pop:", stack.pop()) # Output: C
print("Peek:", stack.peek()) # Output: B
print("Size:", stack.size()) # Output: 2
print("Is empty?", stack.is_empty()) # Output: False
