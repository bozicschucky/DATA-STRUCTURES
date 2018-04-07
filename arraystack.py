class Empty(Exception):
    """
    Error attempting to access an element from an empty container
    """
    pass
    


class ArrayStack:
    """
    LIFO stack implementation using a python list as underlying storage.
    """

    def __init__(self):
        """
        Create an empty stack
        """
        self._data=[]       #non public list
    
    def __len__(self):
        """
        return the number of elements in the stack
        """
        return len(self._data)

    def is_empty(self):
        """
        Return true if the stack is empty.
        """
        return len(self._data)==0

    def push(self,e):
       """
       Add element r to the top of the stack
       """ 
       self._data.append(e)     #new item stored at the end of the list

    def top(self):
        """
        Return (but do not remove) the element at the top of the stack

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]       #last item in the list

    def pop(self):
        """
        Remove and return the element from the top of the stack (i.e, LIFO)

        Raise Empty exception if the stack is empty
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()     #remove last item from list


def reverse_file(filename):
    """
    Overwrite given file with it's contents line-by-line reversed
    """
    S=ArrayStack()
    original=open(filename)
    for line in original: 
        S.push(line.rstrip('\n'))   #we will reinsert new lines when writing
    original.close()

    #now we overwrite   with contents in LIFO order
    output = open(filename,'w')  #reopening files overwrites original
    while not S.is_empty():
        output.write(S.pop()+'\n') #re-insert new line characters
    output.close()


"""
An algorithm for matching delimiters : Applications of stacks
"""
def is_matched(expr):
    """
    test Expression [(5+x)-(y+z)]
    Return true if all delimiters are properly matched; False other wise
    """
    lefty='({['         #opening delimiters
    righty= ')}]'       #closing delimiters
    S = ArrayStack()
    for c in expr:
        if c in lefty:
            S.push(c)   #push left delimiter on stack
        elif c in righty:
            if S.is_empty():
                return False
            if righty.index(c) != lefty.index(S.pop()):
                return False        #mismatched
    return S.is_empty()         #were all symobols matched ?


def is_matched_html(raw):
    """
    Validator for html tags
    Return true if all HTML tags are properly mtached; False otherwise
    """
   S=ArrayStack()
   j = raw.find('<')    #find first '<' character (if any)
   
   while j!=-1:
        k = raw.find('>',j+1)   #find next '>' character
        if k == -1:
            return False        #invalid tag
        tag = raw(j+1:k)        #strip away <>
        if not tag.startswith('/'):     #this is opening tag
            S.push(tag)
        else:
            if S.is_empty():        #this is the closing tag
                return False    #nothing to match with
            if tag[1:] != S.pop():
                return False    #mismatched delimiter
        j=raw.find('<',k+1)     #find next '<' character (if any)
    return S.is_empty()         #were all opening tags matched?


def main():
    S=ArrayStack()
    S.push(5)
    S.push(3)
    print(len(S))
    print(S.pop())
    print(S.is_empty())
    S.push(7)
    S.push(9)

if __name__ == '__main__':
    main()