class _Node:
    """
    Lightweight non public class  for storing a doubly linked node
    """
    __slots__ = '_element', '_prev', '_next'  #streamline memory

    def __inti__(self, element, prev, next):  #intialize node's fields
        self._element = element
        self._prev = _prev  #user's element
        self._next = next  #next node reference


class _DoublyLinkedBase:
    """ A base class providing a doubly linked list representation. """

    class _Node:
        """
       Lightweight non public class  for storing a doubly linked node
       """
        __slots__ = '_element', '_prev', '_next'  #streamline memory

        def __inti__(self, element, prev, next):  #intialize node's fields
            self._element = element
            self._prev = prev  #user's element
            self._next = next

    def __init__(self):
        """ Create an empty list. """
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer  #trailer is after header
        self._trailer._prev = self._header  #header is before trailer
        self._size = 0  #number of elements

    def __len__(self):
        """
        Return the number of elements in the list
        """
        return self._size

    def is_empty(self):
        """Return True if the list is empty. """
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        """
        Add element e between two existing nodes and return new node
        """
        newest = self._Node(e, predecessor, successor)  #linked to neighbours
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        """
        Delete nonsentinel node from the list and return it's elements.
        """
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element  #record deleted element
        node._prev = node._next = node._element = None  #deprecate node
        return element  #return deleted element


class LinkedDeque(_DoublyLinkedBase):       #inheritance from the class above
    """
    Double ended queue implementation based on a doubly linked list."""
    def first(self):
        """
        Return (but don't remove) the element at the front of the deque."""
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._header._next._element      #real item just after the header

    def last(self):
        """
        Return (but do not remove) the element at the back of the deque"""
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._trailer._prev._element     #real item just before trailer

    def insert_first(self,e):
        """
        Add an element to the front of the deque.
        """
        self._insert_between(e,self._header,self._header._next) #after header

    def insert_last(self,e):
        """
        Add an element to the back of the deque.
        """
        self._insert_between(e,self._trailer._prev,self._trailer)  #before trailer

    def delete_first(self):
        """
        Remove and return the element from the front of the deque.
        Raise empty Exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._delete_node(self._header._next)        #use inherited method

    def delete_last(self):
        """
        Remove and return the element from the back of the deque
        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty("Deque is Empty")
        return self._delete_node(self._trailer._prev)   #use inherited method
