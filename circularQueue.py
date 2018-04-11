class CircularQueue:
    """Queue implementation using circularly linked list for storage"""

    class _node:
        """
        Light weight , non public class for storing a singly linked node.
        """
        pass

    def __init__(self):
        """
        Create an empty queue.
        """
        self._tail = None  # will represent tail of queue
        self._size = 0  # number of queue elements

    def __len__(self):
        """
        Return the number of elements in a queue
        """
        return self._size

    def is_empty(self):
        """
        Return True if queue is empty
        """
        return self._size == 0

    def first(self):
        """
        Return the element at the front of the queue.
        Raise Empty exception if the queue is empty
        """
        if self.is_empty():
            raise Empty('Queue is Empty')
        head = self._tail._next
        return head._element

    def dequeue(self):
        """Remove and return the first element of the queue(i.e FIFO)
            Raise Empty exception if the queue is empty
        """
        if self.is_empty():
            raise Empty("Queue is empty")
        oldhead = self._tail._next
        if self._size == 1:  # removing only element
            self._tail = None  # queue becomes empty
        else:
            self._tail._next = oldhead._next  # by pass the old head
        self._size -= 1
        return oldhead._element

    def enqueue(self, e):
        """
        Add element to the back of the queue
        """
        newest = self._node(e, None)  # node will be new tail node
        if self.is_empty():
            newest._next = newest  # intialize circulary
        else:
            newest._next = self._tail._next  # new node points to head
            self._tail._next = newest  # old tail points to new node
        self._tail = newest  # new node becomes the tail
        self._size += 1

    def rotate(self):
        """Rotate the front element to the back of the queue."""
        if self._size > 0:
            self._tail = self._tail._next  # old head becomes new tail
