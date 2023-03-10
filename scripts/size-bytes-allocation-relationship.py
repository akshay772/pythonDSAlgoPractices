import sys

# set n
n = 50

data = []

for i in range(n):
    # number of elements
    a = len(data)

    # actual size in bytes
    b = sys.getsizeof(data)

    print('Length : {0:3d}; Size in bytes: {1:4d}'.format(a, b))

    # increase the length by one
    data.append(n)
