import sys #provides sizeof function
data = []
for k in range(28):
    a=len(data)   #number of elements
    b =sys.getsizeof(data) #actual size in bytes
    print('Lenght:{0:3d}; size in bytes: {1:4d}'.format(a,b))
    data.append(None)     #inrease length by one
