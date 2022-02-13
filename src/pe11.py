############################################################################################################################
#
# Problem 11
#
# In the 20×20 grid below, four numbers along a diagonal line have been marked in red.
# The product of these numbers is 26 × 63 × 78 × 14 = 1788696
# 
# What is the greatest product of four adjacent numbers in the same direction 
# (up, down, left, right, or diagonally) in the 20×20 grid?
#
# Ans: 70600674
############################################################################################################################
from typing import List


def read_data(filename: str="../data/p011_number_grid.txt"):
    '''Attempts to read in the passed filename and returns its contents'''
    with open(filename) as blob:
        return blob.readlines()
        
def clean(text: List[str]) -> List[int]:
    '''Utility function to clean the text data'''
    for i,line in enumerate(text):                 # Read line by line
        text[i] = line.replace('\n','').split(" ") # Remove '\n' and split elements by spaces into a list
    for i, row in enumerate(text):                
        for j, element in enumerate(row):          # Read elements in a given line
            text[i][j] = int(element)              # Cast elements to integers
    return text

def north(i,j):
    idxs = []
    if i - 3 >= 0:
        idxs += [(x, j) for x in range(i, i-4, -1)]
    return idxs
    
def south(i,j,r):
    idxs = []
    if i + 3 < r:
        idxs += [(x, j) for x in range(i, i+4, 1)]
    return idxs
    
def east(i,j,c):
    idxs = []
    if j + 3 < c:
        idxs += [(i, x) for x in range(j, j+4, 1)]
    return idxs

def west(i,j):
    idxs = []
    if j - 3 >= 0:
        idxs += [(i, x) for x in range(j, j-4, -1)]
    return idxs

def northeast(i,j,c):
    idxs = []
    # conditions for east and north boundaries
    if i - 3 >= 0 and j + 3 < c:
        idxs += [(i-up, x) for up,x in enumerate(range(j, j+4, 1))]
    return idxs

def northwest(i,j):
    idxs = []
    # conditions for west and north boundaries
    if j - 3 >= 0 and i - 3 >= 0:
        idxs += [(i-up, x) for up,x in enumerate(range(j, j-4, -1))]
    return idxs

def southeast(i,j,r,c):
    idxs = []
    # conditions for east and south boundaries
    if i + 3 < r and j + 3 < c:
        idxs += [(i+down, x) for down,x in enumerate(range(j, j+4, 1))]
    return idxs

def southwest(i,j,r):
    idxs = []
    # conditions for west and south boundaries
    if j - 3 >= 0 and i + 3 < r:
        idxs += [(i+down, x) for down,x in enumerate(range(j, j-4, -1))]
    return idxs


def directions(i: int, j: int, shape):
    '''
    Args:
        i (int >= 0): the index of the row to consider
        j (int >= 0): the index of the column to consider
        shape (tuple(int,int)): the shape of the grid
    Returns:
        List[List[tuples]]: a nested list of the indices of valid multiplications 
                            in the cardinal and 4 diagonal directions, given a 
                            single element in the matrix: N,S,E,W,NE,SE,SW,NW
    '''
    indices = []
    r,c = shape[0], shape[1]
    # Call all the direction functions to get lists of indices
    func_calls = [north(i,j), 
                  south(i,j,r), 
                  east(i,j,c), 
                  west(i,j), 
                  northeast(i,j,c), 
                  southeast(i,j,r,c), 
                  southwest(i,j,r), 
                  northwest(i,j)]
    for call in func_calls:
        if call != []:
            indices += [call] 
    return indices

def max_prod_in_grid(matrix: List[List[int]]) -> int:
    '''
    Parameters
    ----------
    matrix : List[List[int]]
        An nxn nested list of integers.
    Returns
    -------
    int
        The greatest product of four adjacent numbers in the same direction 
        (up, down, left, right, or diagonally) in the nxn grid.
    '''
    n,m = len(matrix), len(matrix[0])
    prod = []
    for row in range(n):                      # Iterate over each row vector
        for col in range(m):             # Iterate over element in a given row     
            for vector in directions(row,col,(n,m)): # Iterator over the list of valid directions
                temp = 1
                for idx in vector:                   # Iterate over a singe direction vector in list of valid directions 
                    temp *= int(matrix[idx[0]][idx[1]]) # Cast element at index in the direction vector to int and multiply 
                prod.append(temp)
    return max(prod) 


if __name__ == "__main__":            
    print(max_prod_in_grid(clean(read_data())))