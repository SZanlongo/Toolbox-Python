# Lists

# List of Lists
# Create 2-dimensional matrix
lst_2d = [[0] * 3 for i in xrange(3)]
print lst_2d

# Assign a value within the matrix
lst_2d[0][0] = 5
print lst_2d



# Enumerate
# Allows you to have access to the indexes of the elements within a for loop
l = ['a', 'b', 'c', 'd', 'e', 'f']
for (index, value) in enumerate(l):
    print index, value



# Transpose an iterable
a = [[1, 2, 3], [4, 5, 6]]
print zip(*a)

# Same with dicts
d = {"a":1, "b":2, "c":3}
print zip(*d.iteritems())



# Flatten a list of lists
lol = [['a', 'b'], ['c'], ['d', 'e', 'f']]
for outer in lol:
    for inner in outer:
        print inner



# Find out if line is empty
line = ""
if not line.strip():
    print 'empty'

# Remove duplicates from a List
L = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print list(set(L))



# Get integers from a string (space seperated)
S = "1 2 2 3 3 3 4 4 4 4"
print [int(x) for x in S.split()]



# Finding Factorial
fac = lambda(n):reduce(int.__mul__, range(1, n + 1), 1)



# Finding greatest common divisor
def gcd(a, b):
    while(b):
        a, b = b, a % b
    return a
print gcd (54, 24)
