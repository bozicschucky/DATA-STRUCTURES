def binary_sum(S, start, stop):
    """
    Return the sum of the numbers in implicit slice S[start:stop]
    """

    if start >=stop:   #zero elements in slice
        return 0
    elif start == stop-1 : #one element in the slice
        return S[start]
    else:
        mid = (start+stop)//2   #two or more elements in slice
        return binary_sum(S,start,mid) + binary_sum(S,mid,stop)
