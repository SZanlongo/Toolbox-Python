### Lists ###

# List of Lists #
# https://stackoverflow.com/questions/691946/short-and-useful-python-snippets
# Create 2-dimensional matrix
lst_2d = [[0] * 3 for i in xrange(3)]
print lst_2d

# Assign a value within the matrix
lst_2d[0][0] = 5
print lst_2d



# Enumerate #
# https://stackoverflow.com/questions/691946/short-and-useful-python-snippets
# Allows you to have access to the indexes of the elements within a for loop
l = ['a', 'b', 'c', 'd', 'e', 'f']
for (index, value) in enumerate(l):
    print index, value



# Transpose an iterable #
# https://stackoverflow.com/questions/691946/short-and-useful-python-snippets
a = [[1, 2, 3], [4, 5, 6]]
print zip(*a)

# Same with dicts
d = {"a":1, "b":2, "c":3}
print zip(*d.iteritems())



# Flatten a list of lists #
# https://stackoverflow.com/questions/691946/short-and-useful-python-snippets
lol = [['a', 'b'], ['c'], ['d', 'e', 'f']]
for outer in lol:
    for inner in outer:
        print inner



# Find out if line is empty #
# https://stackoverflow.com/questions/691946/short-and-useful-python-snippets
line = ""
if not line.strip():
    print 'empty'



# Remove duplicates from a List #
# https://stackoverflow.com/questions/691946/short-and-useful-python-snippets
L = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print list(set(L))



# Get integers from a string (space seperated) #
# https://stackoverflow.com/questions/691946/short-and-useful-python-snippets
S = "1 2 2 3 3 3 4 4 4 4"
print [int(x) for x in S.split()]



# # Create an n-dimensional array ##
# https://gist.github.com/alexholehouse/6190193#file-gistfile1-py
# Main function to call
# typeOfitem
#     Should be a class which can generate objects
#     e.g. float, int, complex, or any other type, such as
#     myCoolClass
#
# dimensions
#     value for a 1D array, or a list or tuple defining the
#     dimensions, for higher order arrays. e.g. a 3D array
#     might be [2,3,4]
#
def nDarray(typeOfitem, dimensions):
    depth = 0
    if type(dimensions) == int:
        dimensions = [dimensions]
    return(recursiveAllocator(typeOfitem, dimensions, depth))

# Recursive internal function
def recursiveAllocator(basetype, dimensionList, depth):
    # Base case
    if depth == len(dimensionList) - 1:
        currentDimension = dimensionList[depth]
        array = []
        for i in xrange(0, currentDimension):
            array.append(basetype())
        return array

    # Recursive case
    else:
        array = []
        currentDimension = dimensionList[depth]
        # for each element in each dimension recursively
        # call the function
        for i in xrange(0, currentDimension):
            array.append(recursiveAllocator(basetype, dimensionList, depth + 1))
        return array



# Split a list into evenly sized chunks
# https://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks-in-python
l = range(1, 1000)

def chunks(l, n):
    # Yield successive n-sized chunks from l
    for i in xrange(0, len(l), n):
        yield l[i:i + n]

import pprint
pprint.pprint(list(chunks(range(10, 75), 10)))
