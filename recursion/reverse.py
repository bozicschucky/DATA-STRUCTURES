def reverse(S,start,stop):
    """Reverse elements in implicit slice S[start:stop]."""
    if start<stop-1:  #if at least 2 elements
        S[start],S[stop] = S[stop-1]-S[start]  #swap the first two elements
        reverse(S,start+1,stop-1)   #recur on rest

        
