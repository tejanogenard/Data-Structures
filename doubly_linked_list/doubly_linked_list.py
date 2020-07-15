"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def get_value(self):
        return self.value

    def set_value(self):
        self.value = value
    
    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

    def get_prev(self): 
        return self.prev

    def set_prev(self, new_prev):
        self.prev = new_prev
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        if self.head is None:
            new_node = ListNode(value)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = ListNode(value)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None
        

        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        pass
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        if self.head is None:
            new_node = ListNode(value)
            new_node.prev = None
            self.head = new_node
        else: 
            new_node = ListNode(value)
            current = self.head
            while current.next:
                current = current.next
            new_node.prev = current
            new_node.next = None
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        pass
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        pass
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        pass

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        current = self.head
        while current:
            # Do Not loop this use each case to write in the appropriate functions above
                if current.value == node and current == self.head:
                    #case 1: Single node in the linked list
                    if not current.next:
                        current = None 
                        self.head = None 
                        return
                    #case 2: Deleting a head node of a linked list
                    else:
                        nxt = current.next
                        current.next = None 
                        nxt.prev = None 
                        current = None 
                        self.head = nxt
                        return

                elif current.value == node:
                    #case 3: Deletes the input node from the List, preserving the list
                    if current.next:
                        nxt = current.next
                        prev = current.prev
                        prev.next = nxt 
                        nxt.prev = prev
                        current.next = None 
                        current.prev = None
                        current = None 
                        return
                        #case 4: Deleting a tail node of a linked list 
                    else:
                        prev = current.prev 
                        prev.next = None 
                        current.prev = None 
                        current = None
                        return
                    


    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        pass