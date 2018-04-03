class Progression(object):
    """

    Iterator producing a generic progression
    Default iterator produces the whole numbers 0,1,2,..


    """

    def __init__(self, start=0):
        """

        Intialize current to the first value of the progression.

        """
        self._current = start

    def _advance(self):
        """
        Update self._current to a value.

        This should be overridden by a subclass to cutomize progression.

        By Convention , if current is set to None, this designates the end of
        a finite progression.


        """
        self._current += 1

    def __next__(self):
        """
        Return the next element, or else raise a StopIteration error.

        """

        if self._current is None:  # Our convention to end a progression
            raise StopIteration()

        else:
            answer = self._current  # Record currenr value to return
            self._advance()  # advance to prepare for next time
            return answer  # return the answer

    def __iter__(self):
        """
        By conventin, an iterator must return itself as an iterator.

        """
        return self

    def print_progression(self, n):
        '''
        Print next n values of the progression,
        '''

        print(''.join(str(next(self) for j in range(n))))


class ArthmeticProgression(Progression):  # inherit from Progression
    """ Iterator producing an arthimetic progression. """

    def __init__(self, increment=1, start=0):
        """

        Create a new arithmetic progression
        increment  the fixed constant to add to each term( dafault 1)
        start       the first term of the progression (default 0)

        """
    super().__int__(start)      #initialize base class
    self._increment = increment

    def _advance(self):
        """
            Update current value by adding the fixed increment.

        """
        self._current += self._increment


class GeometricProgression(Progression):      #inherit from Progression
    """ Iterator producing an Geometric progression. """
    def __init__(self, base=2,start=1):
        """

        Create a new geometric progression
        base  the fixed constant muiltiplied to each term( dafault 2)
        start       the first term of the progression (default 1)

        """
    super().__int__(start)      #initialize base class
    self._base = base

    def advance(self):
        """
            Update current value by multiplying it by a geometric progression.

        """
        self._current *= self._base



class FibonacciProgression(Progression):
    """Iterator producing a genralized  Fibonacci Progression"""
    def __init__(self, first=0, second=1):
        """
        Create a new fibonnaci progression.

        first    the first term of the progression (Default 0)
        second   the second term of the progression (Default 1)
        super(FibonacciProgression, self).__init__()
        """
        super().__init__(first)     #start progression at first
        self._prev = second - first  #fictious value preceding the first
        


    def _advance(self):
        """
        Update current value by taking sum of previouus two 
        """
        self._prev,self._current =self._current,self._prev + self._current


if __name__ == '__main__':
    print('Default progression:')
    Progression().print_progression(10)

    print('Arthimetic progression with increement 5:')
    ArthmeticProgression(5).print_progression(10)

    print('Arthimetic progression with increement 5 and start 2:')
    ArthmeticProgression(5,2).print_progression(10)
    print('Geometric progression with default base:')
    GeometricProgression().print_progression(10)
    print('Geometric progression with base 3')
    GeometricProgression(3).print_progression(10)
    print('Fibonacci Progression with default start values:')
    FibonacciProgression().print_progression(10)
    print('Fibonacci Progression with start values 4 and 6:')
    FibonacciProgression(4,6).print_progression(10)
