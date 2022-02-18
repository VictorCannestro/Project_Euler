##############################################################################
#
# Problem 3
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
#
# Ans: 6857
##############################################################################

def isPrime(num: int) -> bool:
    '''
    Args:
        num (int): number to check if prime
    Returns:
        (bool): True if prime, false if not
    '''
    if num < 1:
        raise ValueError("Please enter a natural number.")
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
        for i in range(2, num//2+1): # Check if i divides the first half of num
            if num % i == 0:
                return False
        return True


def listProduct(nums):
    '''
    Args:
        nums (list): list of integers
    Returns:
        prod (int): product of all list elements
    '''
    prod = 1
    for i in nums:
        prod *= i
    return prod 


def getPrimeFactors(n=600851475143):
    i = 2
    factors = []
    temp = n
    # Iterate until list of factors multiples to n
    while listProduct(factors) != n:
        if temp % i == 0:     # If i is a factor then append
            factors.append(i)
            temp //= i        # update by dividing by i
        else:
            i += 1            # i is not a factor so check next    
    return factors
 
    
if __name__ == "__main__":
    print(getPrimeFactors()[-1])