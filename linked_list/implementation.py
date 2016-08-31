from .interface import AbstractLinkedList
from .node import Node

class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList inteface.
    """

    def __init__(self, elements=None):              #Initializer, defaults with a None object
        self.start = None                           #Set the starting node and the last one.
        self.end = None
        self.size = 0
        if elements is not None:                    #Checking if there was any objects passed
            if isinstance(elements, list):          #Checking if a list object was passed
                if elements:                        #Checking if the list is empty
                    self.start = Node(elements[0])  #Setting the first node as the first object in the list that was passed
                    self.size += 1
                    position = self.start
                    for element in elements[1:]:    #Iterating through the list that was passed except the first object
                        new_node = Node(element)    #Create a new node each time, and setting the position to the next node
                        position.next = new_node
                        position = new_node
                        self.size += 1
                    self.end = position
            else:
                new_node = Node(elements)           #If not a list, we simply create a single node with the object passed and set it as the first node
                self.start = new_node
                self.end = new_node
                self.size += 1
            
            
    def __str__(self):
        if self.start is not None:                  #Checks if the linked list is empty
            position = self.start                   #Setting position to the first node and creates a temporary list
            list = []
            while position is not None:             #Iterates to the end of the linked list and appends the elements of each node to the temporary list
                list.append(position.elem)
                position = position.next
            return '{}'.format(str(list))
        else:
            return '[]'                             #Returns a represantion of an empty list if the linked list is indeed empty


    def __len__(self):
        return self.count()                         #Uses the count method to return the length of the linked list


    def __iter__(self):
        position = self.start
        while position is not None:
            yield position.elem
            position = position.next


    def __getitem__(self, index):
        if len(self) - 1 < int(index):
            raise IndexError
        
        position = self.start
        counter = 0
        while counter < index:
            position = position.next
            counter + 1
        return position.elem


    def __add__(self, other):
        new_list = LinkedList()
        
        for element in self:
            new_list.append(element)
        
        for element in other:
            new_list.append(element)
        
        return new_list
        
        
    def __iadd__(self, other):
        for element in other:
            self.append(element)
        return self


    def __eq__(self, other):
        if len(self) != len(other):
            return False
        
        position = self.start
        other_position = other.start
        counter = 0
        while counter < len(self):
            if position.elem != other_position.elem:
                return False
            else:
                position = position.next
                other_position = other_position.next
                counter += 1
        
        return True
    
    
    def __ne__(self, other):
        return not self is other
    
        
    def append(self, elem):
        new_node = Node(elem)                       #Creating a new node to add to the linked list
        if self.start is None:                      #Checks if the linked list is empty, and sets the new node as first
            self.start = new_node
            self.end = new_node
        else:                                       #If the linked list is not empty, adds the new node to the end and connects the second last one to it
            self.end.next = new_node
            self.end = self.end.next
        self.size += 1

    def __repr__(self):
        return str(self)

    def count(self):
        return self.size
        

    def pop(self, index=None):
        if self.start is None:                      #Raise exceptions if the linked is empty or if the index specified is larger than the length of the linked list
            raise IndexError
        
        if index is not None:                                  
            if len(self) - 1 < index:
                raise IndexError
            
            previous_node = None                    #Setting the position to the first node and creating a counter
            position = self.start
            counter = 0
            element = position.elem
        
            while position and counter < index:     #Iterates through the linked list until the index value passed matches the counter
                previous_node = position
                position = previous_node.next
                counter += 1
                element = position.elem
        
            if previous_node == None:               #If the first node is popped, sets the next one node as the first
                self.start = position.next
                self.size -= 1
                return element
            else:                                   #If it's not the first node, links the node before the one popped to the next one
                previous_node.next = position.next
                self.size -= 1
                return element
        else:                                        #If there is no index passed, pop the last node in the linked list
            element = self.end.elem
            if len(self) - 1 is 1:
                self.first = None
                self.size -= 1
            else:
                self.end = None
                self.size -= 1
            return element