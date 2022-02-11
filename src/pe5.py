'''
 Problem 5

 2520 is the smallest number that can be divided by each of 
 the numbers from 1 to 10 without any remainder.

 What is the smallest positive number that is evenly divisible 
 by all of the numbers from 1 to 20?


 Notes: Let's make a table of the first 15 inputs/outputs of the brute force approach 
        to see if we can find a pattern.
 
       | Disvisible up to | 1 | 2 | 3 | 4  | 5  | 6  | 7   | 8   | 9    | 10   | 11    | 12    | 13     | 
       |------------------|---|---|---|----|----|----|-----|-----|------|------|-------|-------|--------|
       | Output           | 1 | 2 | 6 | 12 | 60 | 60 | 420 | 840 | 2520 | 2520 | 27720 | 27720 | 360360 |

       Notice that some outputs are repeated for different values. Let's try and 
       leverage that and strive to express the output as an online update instead 
       of being computed from scratch at each stage.
       
       | Output           | 1 | 2 | 6 | 12 | 60 | 60 | 420 | 840 | 2520 | 2520 | 27720 | 27720 | 360360 |
       |------------------|---|---|---|----|----|----|-----|-----|------|------|-------|-------|--------|
       |Output(n-1)*factor|*1 |*2 |*3 | *2 | *5 |    | *7  | *2  | *3   |      | *11   |       | *13    | 
       
       Strategy: [x] Compute Result(n-1)
                 [x] Check if Result(n-1) divides n as well
                     [x] If yes, return Result(n-1)
                     [x] Else, check Result(n-1)*smallest_prime_factor_of(n)
                     
 Ans: 232792560
'''
import math 


def prime_factors_set(n: int) -> set:
        '''Utillity function to get the prime factor decomposition of n'''
        factors = set()
        while n % 2 == 0:
            factors.update([2])
            n = n / 2   
        for i in range(3, int(math.sqrt(n))+1, 2): # n became odd
            while (n % i == 0):
                factors.update([i])
                n = n / i
        if n > 2:
            factors.update([int(n)])
        return factors 
    
    
def brute_force(d: int) -> int:
    '''
    Args:
        d (int > 0): the upper bound of the consecutive divisors  
    Returns:
        (int): the smallest positive number that is evenly divisible 
               by all of the numbers from 1 to d
    '''
    if d < 1:
        raise ValueError("Must input a positive integer.")
    elif d == 1:
        return 1
    smallest = d * (d-1)
    # A generator comprehension that checks if smallest divides the numbers 
    # from 1 to d without any remainder. Contains boolean values. 
    while sum(smallest % i == 0 for i in range(1, d+1)) != d:
        smallest += 1
    return smallest   

def smallest_evenly_divisible(d: int) -> int:
    '''
    Parameters
    ----------
        d : (int > 0) the upper bound of the consecutive divisors 
    Returns
    -------
    int
        The smallest positive number that is evenly divisible by all of the 
        numbers from 1 to d.    
    '''
    if d < 1:
        raise ValueError("Must input a positive integer.")
    elif d == 1:
        return 1
    else:
        calc = smallest_evenly_divisible(d-1)
        if calc % d == 0:
            return calc
        else:
            return calc * min(prime_factors_set(d))


if __name__ == "__main__":
    print(smallest_evenly_divisible(20))