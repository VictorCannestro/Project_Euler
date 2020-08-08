#!/usr/bin/env python
# coding: utf-8

# In[1]:


# In the 20×20 grid below, four numbers along a diagonal line have been marked in red.
# The product of these numbers is 26 × 63 × 78 × 14 = 1788696
# 
# What is the greatest product of four adjacent numbers in the same direction 
# (up, down, left, right, or diagonally) in the 20×20 grid?

import numpy as np

matrix = '''08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
            49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
            81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
            52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
            22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
            24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
            32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
            67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
            24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
            21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
            78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
            16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
            86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
            19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
            04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
            88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
            04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
            20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
            20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
            01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48'''

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
                
    Notes:
    '''
    indices = []
    r,c = shape[0], shape[1]
    
    # Call all the direction functions to get lists of indices
    func_calls = [north(i,j), south(i,j,r), east(i,j,c),west(i,j), northeast(i,j,c), 
                  southeast(i,j,r,c), southwest(i,j,r), northwest(i,j)]
    for call in func_calls:
        if call != []:
            indices += [call] 
    return indices
    
# Parse the 20x20 block of numbers into a numpy array of strings
matrix = [row.split(' ') for row in matrix.replace('           ','').split('\n ')]
arr = np.array(matrix)

# Get the shape of the array for later processing
n,m = np.shape(arr)

prod = []
for row in range(len(arr)):          # iterate over each row vector
    for col in range(len(arr[row])): # iterate over element in a given row     
        for vector in directions(row,col,(n,m)): # iterator over the list of valid directions
            temp = 1
            for idx in vector: # Iterate over a singe direction vector in list of valid directions
                temp *= int(arr[idx[0], idx[1]]) # cast element at index in the direction vector to int and multiply 
            prod.append(temp)
            
print(max(prod))


# In[2]:


test = [(6,8),(7,9),(8,10),(9,11)]

def test1(t):
    assert t in directions(6,8,(20,20))
    
def test2(array, t):
    a = int(array[t[0][0], t[0][1]]) # should be 26
    b = int(array[t[1][0], t[1][1]]) # should be 63
    c = int(array[t[2][0], t[2][1]]) # should be 78
    d = int(array[t[3][0], t[3][1]]) # should be 14
    assert a*b*c*d == 1788696
    
test1(test)
test2(arr, test)


# In[ ]:




