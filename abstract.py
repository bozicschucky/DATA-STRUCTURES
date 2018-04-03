from abc import ABCMeta, abstractmethod   # need these imports


class Sequence(metaclass = ABCMeta):
    """Our own version of collections abstarct

    base class
    """

    @abstractmethod
    def __len__(self):
        '''Return the lenght of the seequence.'''

    @abstractmethod
    def __getitem__(self,j):
        """
        Return the element of index j of the seqence
        """

    def __contains__(self,j):
        """
        Return True if val found in the Sequence;
        False otherwise.
        """

        for j in range(len(self)):      #found match
            if self[j] == val:
                return True
        return False


    def index(self,val):
        """
        Return leftmost index at wich val is found( or raise ValueError)

        """

        for j in range(len(self)):
            if self[j] == val:          #leftmost match
                return j
        raise ValueError('Value not in Sequence') #never found a match

    def count(self,val):
        """
        Return the number of elements equal to given value
        """
        k=0
        for j in range(len(self)):
            if self[j] == val:
                k+=1
        return k


