"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        #1. base case 
            # if the value of this node matches the target, then TRUE 
            # compare the target against this node's value to determine which direction to go in
        #2. how do we move closer to the base case
            # if the target is less 
                #if left is Null
                #value is not contained in the tree 
                # else call 'contains' on the left child 
            #else if the target is more 
                #if right is Null
                #value is not contaied in the tree 
                # else call 'contains' on the right child

        if target == self.value:
            return True
        elif target < self.value:
            if self.left is None:
                return False
            else: 
                return self.left.contains(target)
        else:
            if self.right is None:
                return False 
            else: 
                return self.right.contains(target)
        

    # Return the maximum value found in the tree
    def get_max(self):
        #Check the right most value in the tree 
        # we'll keep going right until there is no right child node 

        if self.right is None:      #base case
            return self.value
        else:
            return self.right.get_max() #recurisve statement

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # call the anonymous function on 'self.value'
        # if this node has a left child 
            #pass the anonymous fn to it
        #if this node has a right child 
            #pass the anonymous fn to it 
            
        fn(self.value)
        if self.right is not None:
            self.right.for_each(fn)
        if self.left is not None:
            self.left.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
