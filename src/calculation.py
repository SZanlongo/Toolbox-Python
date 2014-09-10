### Calculation ###

# Finding Factorial #
# https://stackoverflow.com/questions/691946/short-and-useful-python-snippets
fac = lambda(n):reduce(int.__mul__, range(1, n + 1), 1)



# Finding greatest common divisor #
# https://stackoverflow.com/questions/691946/short-and-useful-python-snippets
def gcd(a, b):
    while(b):
        a, b = b, a % b
    return a
print gcd (54, 24)
