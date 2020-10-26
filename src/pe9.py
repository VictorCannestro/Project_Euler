############################################################################################################################
#
# Problem 9
#
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a**2 + b**2 = c**2
#
# For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
############################################################################################################################

def findTriplets(n):
    '''
    Args:
        n (int >= 12): the sum of pythagorean triplets
    
    Returns:
        (a,b,c) (tuple): the tuple of pythagorean triplets that sums to n 
    
    Notes:
        We use the fact that c = n - a - b and a < b < c.
    '''
    ts =  [(a, b, n-a-b) for a in range(1,n) for b in range(a,n) if (a**2 + b**2 - (n-a-b)**2 == 0)]
    return ts[0]

def product(ts):
    prod = 1
    for i in ts:
        prod *= i
    return prod

n = 1000
triplets = findTriplets(n)
print(product(triplets))
