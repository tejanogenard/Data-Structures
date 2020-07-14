"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""



# Now do your import
from linked_list import LinkedList
from linked_list import Node


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def push(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def pop(self):
        if self.size > 0:
            x = self.storage.remove_tail()
            self.size -= 1
            return x
        else:
            return None
    
    def __len__(self):
        return self.size

        

# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def push(self, value):
#         self.storage.append(value)
#         return value

#     def pop(self):
#         if len(self.storage) > 0:
#             remove = self.storage[-1]
#             self.storage.pop()
#             return remove
#         else:
#             pass
