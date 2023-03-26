class CircularQueue:
    """Queue implementation using circularly linked list for storage"""""
    
    class _Node:
        __slots__ = '_element', '_next'
        
        def __init__(self, element, nxt):
            self._element = element
            self._next = nxt

    def __init__(self):
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty(): #If the previously created method "is_empty" is true, then an exception is raised
            raise Empty("The queue is currently empty")
        return self._tail._next._element #The "self._tail._next._element" in turn points to the very first element of the queue

    #What if we want to remove the first element from the queue? Don't worry
    def dequeue(self):
        if self.is_empty():
            raise Empty("The queue is currently empty")
        prev_head = self._tail._next #Using same logic from the "first" method, we set a value for the previous head we'll be replacing
        if self._size == 1: #If the queue is only a size of 1, the queue will be set to empty
            self._tail = None
        else:
            self._tail._next = prev_head._next #This allows us to "skip" over the previous head and go to the next element
        self._size -= 1 #Updates the size of the queue accordingly
        return prev_head._element #returns the element that has been removed from the queue
    
    #Now let's create a method that adds an element to the back of the queue
    def enqueue(self, e):
        new_element = self._Node(e, None) 
        if self.is_empty(): #If the queue is empty, then this added element will become the first
            new_element._next = new_element
        else:
            new_element._next = self._tail._next #Setting new_element's next pointer to the current head of a non-empty queue
            self._tail._next = new_element
        self._tail = new_element #Lastly, the tail is now set to this new element and thus becoming the new end element
        self._size += 1 #Updates the size of the queue accordingly
    
    #This method will allow us to transfer the item at the head of the list to the tail of the list
    def rotate(self):
        if not self.is_empty():
            self._tail = self._tail._next #Fairly straightforward, but if the queue isn't empty, then setting the tail equal to the head
   
