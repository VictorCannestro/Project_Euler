'''
Problem 27

Euler discovered the remarkable quadratic formula: n**2 + n + 41. It turns out 
that the formula will produce 40 primes for the consecutive integer values 0 <= n <= 39. 
However, when n=40, 40**2 + 40 + 41 is divisible by 41, and certainly when n=41, 41**2 + 41 + 41 
is clearly divisible by 41.

The incredible formula n**2 -79*n + 1601 was discovered, which produces 80 primes 
for the consecutive values 0 <= n <= 79.  The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n**2 + a*n + b, where |a| < 1000 and |b| <= 1000

where |n| is the modulus/absolute value of n, e.g. |-11|=11 and |11|=11.

Find the product of the coefficients, a and b, for the quadratic expression that produces 
the maximum number of primes for consecutive values of n, starting with n=0.

Ans: 
'''

def is_prime(num: int) -> bool:
    '''
    Parameters
    ----------
    x : int
        A positive natural number.
    Raises
    ------
    ValueError
        When the input is not a natural number.
    Returns
    -------
    bool
        Whether the input x is prime or not.
    '''
    if num < 1:
        raise ValueError("Please enter a natural number.")
    elif num == 2:
        return True
    elif num % 2 == 0 or num == 1:
        return False
    else:
        for i in range(2, num//2+1): # Check if i divides the first half of num
            if num % i == 0:
                return False
        return True

def eratosthenes(n: int) -> set:
    '''
    Args:
        n (int > 0): the upper bound of primes to consider   
    Returns:
        (generator): of prime numbers <= n
    '''
    multiples = set()                            # Use set to have unique elements
    for i in range(2, n+1):                                         
        if i not in multiples:                   # Multiples are not primes, so all leftovers are                      
            yield i                              # Yield the next prime number
            multiples.update(range(i*i, n+1, i)) # Add to the list of integer multiples: [i**2,n] in steps of i

def find_coefficients(N: int, prime_map: dict) -> list:
    '''
    Parameters
    ----------
    N : int
        The range of natural number coefficients to consider, i.e. (-N, N).
    prime_map : dict
        A dictionary of natural numbers whose boolean values correspond to 
        whether a particular natural number is prime or not.
    Returns
    -------
    list
        Of the coefficients, c0 and c1, for the quadratic expression n**2 + c0*n + c1
        that produces the maximum number of primes for consecutive values of n,
        starting with n=0. Also, the length of the longest streak.
    '''
    longest_streak = [0,0]
    primes = [*eratosthenes(N)]              # Precompute primes to use as intercept values
    for a in range(-N+1, N):                 # a in (-N, N)
        for b in primes:                     # b in primes subset of [-N, N], since @ n=0 the streak must start
            n, streak = 0, 0
            while prime_map.get(n**2 + a*n + b, False): # While the streak is still going
                n += 1
                streak += 1
            if streak > longest_streak[1]:
                longest_streak = [(a,b), streak]    
    return longest_streak
                    
def calculate_coefficient_prod(info: list) -> int:
    '''Extracts coefficients and calculates the product to get the answer'''
    (a,b), length = info
    return a*b
    

if __name__ == '__main__':
    info = find_coefficients(1000, prime_map={k:is_prime(k) for k in range(1, 10000)})
    print(calculate_coefficient_prod(info))    