class Vector(object):
    """Represent Vector for a multidimensional space """

    def __init__(self, d):
        """Creates d-dimensional vectors of zeros """
        self._coords = [0] * d

    def __len__(self):
        '''Return the dimension of the vector. '''
        return len(self._coords)

    def __getitem__(self, j):
        """
                Return the jth coordinate of a vector
                """
        return self._coords[j]

    def __setitem__(self, j, val):
        """Set jth coordinate of the vector to given values """
        self._coords[j] = val

    def __add__(self, other):
        """
                Return sum of two vectors
                """

        if len(self) != len(other):  # relies on the len method
            raise valueError('dimensions must agree')

        result = Vector(len(self))  # start with a vector of zeros

        for j in range(len(self)):
            result[j] = self[j] + other[j]
            return result

    def __eq__(self, other):
        """
                Return True if vector has same coordinates as other
                """
        return self._coords == other._coords

    def __ne__(self, other):
        """return True if the vector differs from others"""
        return not self == other  # rely on existing __eq__ definition

    def __str__(self):
        """ Produce String representation of the vector """
        return '<' + str(self._coords)[1:-1] + '>'  # adapt list represenation


v = Vector(5)
v[1] = 23
v[-1] = 25
print(v[1])
for entry in v:
    print(entry)
