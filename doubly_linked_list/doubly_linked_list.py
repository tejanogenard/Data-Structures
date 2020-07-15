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
    #create an instance of a listnode with value 
        new_node = ListNode(value)
    #increment the linked list 
        self.length += 1
    #if the list is empty 
        if self.head is None:
    #set head and tail to new node instance
            self.head = new_node
            self.tail = new_node

    #else the list is not empty 
        else:
    #set current head. prev to be new_Node 
            self.head.prev = new_node
    #set new_node.next to be the current head 
            new_node.next = self.head
    #Change the current to be the new_Node
            self.head = new_node
    #set new_node.prev to be None 
            new_node.prev = None
        

        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        #if the list is empty return none 
        if self.length == 0:
            return None 
        #if the list is not empty    
        #store the value of the current head 
        node = self.head
        #decrement the linked list 
        self.length -= 1
        #if the head.next is not none 
        if self.head.next is not None:
        #set the the next nodes prev (head node) to be none 
            self.head.next.prev = None
        #set the new head node 
            self.head = self.head.next 
        else:
            #if head.next is none
            #set head to none 
            # set tail to
            self.head = None
            self.tail = None
        ##return vale 
        return node.value
        
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        #create instance of listnode with value 
        new_node = ListNode(value)
        #increment the length of the list 
        self.length += 1

        #if the list is empty
        if self.head is None:
            #set the new node 
            self.head = new_node
            self.tail = new_node
        #if the list is not empty
        else: 
            #set new node's prev to current tail 
            new_node.prev = self.tail
            #set tail.next to new node 
            self.tail.next = new_node
            #set tail to the new node 
            self.tail = new_node
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        # #if the list is empty
        if self.length == 0:
            return None 
        # #store the value of the current tail
        node = self.tail
        # #decrememnt the length 
        self.length -=1
        # #if tail.prev points to a node
        if self.tail.prev is not None:
        # #set tail.prev.next to none
            self.tail.prev.next = None 
        # #set tail to tail.prev
            self.tail = self.tail.prev 
        else:
            #set head to None 
            self.head = None 
            #set tail to None 
            self.tail = None 

        # #return the value 
        return node.value

            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
    #if node is the tail
        if node is self.tail:
            #set the new tail of the list 
            self.tail = node.prev
            self.tail.next = None 
            #set the head of the listnode 
            node.prev = None
            node.next = self.head
            #change current head to point to new head 
            self.head.prev = node 
            #set the head to the node
            self.head = node 
        else: 
            #arrange the nodes so that the target node is isolated
            node.prev.next = node.next
            node.next.prev = node.prev
            #move and prepare the head node and the node after 
            node.prev = None
            node.next = self.head
            self.head.prev = node
            self.head = node
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
        #if the list is empty return None
        if self.length == 0: 
            return None
        
        #decrement the length 
        self.length -=1 
        #if there is only 1 element in the list 
        if self.head == self.tail:
        #set both to none 
            self.head = None
            self.tail = None 
        #return the value 
            return node.value    
        #if head    
        elif node == self.head:
        #set head to the nezt node 
            self.head = self.head.next 
        #set node to none
            node.next = None 
        #set head.prev to none
            self.head.prev = None 
        #return value
            return node.value
        #if tail 
        elif node == self.tail:
        #set tail to tail.prev 
            self.tail = self.tai.prev 
        #set node.prev to non 
            node.prev = None
        #set the next node pointer to none 
            self.tail.next = None 
        else:
        #set the node.prev
            node_prev = node.prev
        #set the node.next
            node_next = node.next
        #set the node.prev next 
            node.prev.next = node.next
        #set the node.next prev
            node_next.prev = node.prev
            return node.value

        
                    


    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        pass
