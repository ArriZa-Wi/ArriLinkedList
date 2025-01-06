class LinkedList:
    "Linked list data structure"
    
    class Node:
        "A node in a linked list will always need 2 instance variables (attributes):"
        "The data attribute that actually holds the data, and the next attribute that is meant to reference the next node"
        def __init__(self):
            "Constructor for the Node class"
            self.data = None
            self.next = None
    
    def __init__(self):
        "Constructor for the LinkedList class"
        self.head = None
        self.tail = None
        self.size = 0

    @property #This is used to set a method for a class, but will act like a property/attribute. Mainly used for setting/checking the conditions of an instance created using the class
    def is_empty(self):
        "if the head pointer point to nothing (is none), then the is_empty property is fulfilled"
        return self.head is None

    @property
    def size(self):
        "Property for the size"
        return self.size
    
    def add_to_front(self, data):
        "Add a new element to the front of the linked list"
        # Start out by creating a new variable that references the head of the linked list when creating a new instance. When first starting out, this means the self.head is currently pointing to None, so old_head is None as well
        old_head = self.head

        # Make a new node (by using self.Node()) and assign it to the self.head variable.
        self.head = self.Node()

        # self.head is the "name" of the new node. a node will have the data attribute. hence, we are calling self.head.data.
        # We are then setting the data attribute of the self.head node to the "data" argument we receive when calling the add_to_front method.
        self.head.data = data

        # Set the ".next" attribute of the self.head node equal to the old_head. In this case, where we are adding the very first node, the old_head is pointing/equal to None. 
        # In the case of adding a 2nd or more nodes to the LL, the .next attribute
        # of the new self.head node will be assigned/point to the previous node that is currently assigned to old_head
        self.head.next = old_head

        # Increment size of the list
        self.size += 1

        # When adding the very first node to the linked list (in this case, self.head), tail should be pointing to it as well.
        if self.size == 1:
            self.tail = self.head

    def add_to_back(self, data):
        "add a new element to the front of the linked list"
        # Much like the add_to_front method, we start by creating a new variable to be a "placeholder" and assigning it to the self.tail variable. Much like old_head, old_tail will be None when adding the very first node to the linked list.
        old_tail = self.tail

        # Make a new Node and assign it to the self.tail variable.
        self.tail = self.Node()
        


    def remove_from_front(self, data):
        "Remove an element from the front of the linked list"

    def remove_from_back(self, data):
        "remove element from the back of the linked list"

    def __str__(self): # When printing an instance, you get the memory address of the instance. If you want something more readible, you use thge __str__ aka string method.
        return super().__str__()
        

