def binary_search(data, target,low,high):
    """
        Return true if target is found in indicated portion of a python list.
        The search only considers the portion from data[low] to data[high] inclusive
    """
    if low >high:
       return False         #interval is empty; no match

    else:
        mid =(high+low)//2
        if target == data[mid]:   #found a match
             print("Found value = {}".format(target))    
             return True

        elif target < data[mid]:
            #recur on the portion left of the middle
            return binary_search(data,target,low,mid-1) 

        else:
            #recur on the portion right of the middle
            return binary_search(data,target,mid+1,high)


data =[2,4,5,7,8,9,12,14,17,19,22,25,27,28,33,37,700]

print(binary_search(data,70,0,16))
