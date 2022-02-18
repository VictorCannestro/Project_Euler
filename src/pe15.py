############################################################################################################################
#
# Probelm 15
#
# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, 
# there are exactly 6 routes to the bottom right corner.
#
# How many such routes are there through a 20×20 grid?
#
# Ans:  137846528820
############################################################################################################################

from math import factorial


def pathChoices(n: int) -> int:
    '''
    Args:
        n (int > 0): the size of 1 grid dimension
    Returns:
        (int): the number of path choices in an nxn grid if we can only move
               down or right.
    Notes:
        Notice for an nxn grid it takes 2n moves to get to the bottom right corner. 
        We must go down (D) or right (R) n times each and have different ways to
        choose the path: 2n choose n. For example if n=2: 
        (D,D,R,R), (D,R,D,R), (R,R,D,D), (R,D,R,D).
        
        This is also described by the Catalan number:
        
        https://www.wikiwand.com/en/Catalan_number
    '''
    return factorial(2*n) // (factorial(n)*factorial(n))


if __name__ == "__main__":
    print(pathChoices(20))