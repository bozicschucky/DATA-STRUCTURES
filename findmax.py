def find_max(data):
    """
    Return the maximum element from a non empty python list

    """
    biggest = 0  # the intial value to beat
    for val in data:  # for each value:
        print(val)
        if val > biggest:  # if it is greater than the best so far
            biggest = val  # we have found a new best (so far)
        return biggest  # when loop ends, biggest is the max


print(find_max([3, 45, 56, 100]))
