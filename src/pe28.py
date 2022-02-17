'''
Number spiral diagonals
Problem 28

Starting with the number 1 and moving to the right in a clockwise direction a 
5 by 5 spiral is formed as follows:

 (21) 22  23  24 (25)
  20  (7)  8  (9) 10
  19   6  (1)  2  11
  18  (5)  4  (3) 12
 (17) 16  15  14 (13)
 
It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed 
in the same way?

Ans: 669171001
'''

def spiralDiagonals(N: int=3) -> list:
    '''
    Parameters
    ----------
    N : int, optional
        An odd int > 0. The dimensions for an NxN odd numbered grid formed by 
        a CW spiral. The default is 3.
    Returns
    -------
    sequence : list
        The sequence of index numbers found on its diagonals. Leverages the fact
        that the diagonals follow a difference pattern that can be caputured by
        recurrance relations.
    '''
    a = 8                               # Can think of this as "acceleration"
    NE, SE, SW, NW = [1], [1], [1], [1] # Set initial values for sequence on each diagonal
    N_map = (N + 1) // 2                # Map the grid size to the correct index of the sequence e.g. 3x3 grid has 2 diagonal elements in any one direction 
    for i in range(1,N_map):
        NE.append(NE[i-1] + a*(i-1) + 8) # Same as 4i**2 + 4i + 1 
        SE.append(SE[i-1] + a*(i-1) + 2) # Same as 4i**2 - 2i + 1 
        SW.append(SW[i-1] + a*(i-1) + 4) # Same as 4i**2 + 1 
        NW.append(NW[i-1] + a*(i-1) + 6) # Same as 4i**2 + 2i + 1  
    # Same as 1 + \sum_{i=1}^{N_map}{16i**2 + 4i +4}
    sequence = sorted(NE + SE[1:] + SW[1:] + NW[1:]) # ignore repeated 1s
    return sequence


if __name__ == "__main__":
    print(sum(spiralDiagonals(N=1001))) 