class Empty(Exception):
    """docstring for Empty exception class"""
        pass


class LinkedStack:
    """LIFO Stack implementation using a singly linked list for storage"""
   #----------Nested node class-------------
    class _Node(object):
        """Lightweight,non public class for storing a singly linked Node """
        __slots__ = '_element', '_next'  # streamline memory usage

        def __init__(self, element, next):  # initialize node's fields
            self._element = element  # reference to user's element
            self._next = next  # reference to next node

    #-------------stack methods ------------------------
    def __init__(self):
        """ Create an empty stack """
        self._head = None  # reference to the head node
        self._size = 0  # number of stack elements

    def __len__(self):
        """
        Return the number of elements in the stack
        """
        return self._size

    def is_empty(self):
        """
        Return True if the stack is empty
        """
        return self._size == 0

    def push(self, e):
        """
        Add element e to the top of the stack.
        """
        self._head = self._Node(e, self._head)  # create and link a new node
        self._size += 1

    def top(self):
        """
        Return (but don't remove) the element at the top of the stack.
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element  # top of stack is at the head of list

    def pop(self):
         """
        Remove and return the element from the top of the stack (i.e LIFO).
        Raise Empty exception if the stack is empty

         """
        if self.is_empty():
            raise Empty("Stack is empty")
        answer = self._head._element
        self._head = self._head._next   #bypass the former top node
        self._size -= 1
        return answer

class LinkedQueue(object):
    """FIFO queue implemenatation using a singly linked list for storage."""

       #----------Nested node class-------------
    class _Node(object):
        """Lightweight,non public class for storing a singly linked Node """
        __slots__ ='_element','_next'   #streamline memory usage

        def __init__(self, element,next):   #initialize node's fields
            self._element=element       #reference to user's element
            self._next = next           #reference to next node

    def __init__(self):
        """
        Create an empty queue.
        """
        self_.head = None
        self._tail = None
        self._size = 0          #number of queue elements

    def __len__(self):
        """
        Return the number of elements in the queue
        """
        return self._size

    def is_empty(self):
        """
        Return true if the queue is empty.
        """
        return self._size == 0

    def first(self):
        """
        Return (but don't remove) the element at the front of thw queue.
        """
        if self.is_empty:
            raise Empty("Queue is empty")
        return self._head._element  #front aligned with head of list

    def dequeue(self):
        """
        Remove and return the first element of the queue (i.e, FIFO)
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty("Queue is empty"):
            raise Empty("Queue is empty")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():     #special case as queue is empty
            self._tail = None   #removed head had been the tail
        return answer

    def enqueue(self,e):
        """
        Add an element to the back of the queue
        """
        newest = self._Node(e,None)     #node will be new tail node
        if self.is_empty():
            self._head = newest         #special case: preivously empty
        else:
            self._tail._next = newest
            self._tail = newest         #update reference to tail node
            self._size += 1
