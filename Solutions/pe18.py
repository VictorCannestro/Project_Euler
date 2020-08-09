#!/usr/bin/env python
# coding: utf-8

# In[1]:


# By starting at the top of the triangle below and moving to adjacent 
# numbers on the row below, the maximum total from top to bottom is 23.
#
#               3
#              7 4
#             2 4 6
#            8 5 9 3
#
# That is, 3 + 7 + 4 + 9 = 23.
#
# Find the maximum total from top to bottom of the triangle below:
#
# NOTE: As there are only 16384 routes, it is possible to solve 
#       this problem by trying every route.

tri ='''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''

def str2Int(lst):
    '''Converts list of str to list of ints'''
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            lst[i][j] = int(lst[i][j])
    return lst

matrix = tri.replace('\n',',').split(',')
matrix = [row.split(' ') for row in matrix]
matrix = str2Int(matrix)

def findPath(matrix):
    '''
    Args:
        matrix: list of lists of ints
        
    Returns:
        The path of the yielding the maximum total from top
        to bottom of the triangle matrix input
    '''
    # set the initial starting points
    path_idxs = [0]
    path = [int(matrix[0][0])]
    
    # Iterate over each row in matrix, save for the first
    for i in range(1,len(matrix)):
        # record the index of the previous path max
        idx = matrix[i-1].index(path[i-1])
        # List indices of the adjacent elements
        valid_idxs = list(set([abs(idx-1), idx, idx+1]))
        # If a candidate is outside the bounds, drop it
        if valid_idxs[-1] >= len(matrix[i]):
            vaild_idxs.pop(-1)
        
        choices = []
        for k in valid_idxs:
            # Record values of the 2-3 candidates
            choices.append(matrix[i][k])
        
        # Select the largest path element candidate
        v = max(choices)
        path.append(v)
        path_idxs.append(matrix[i].index(v))
        
    return path
                
print(findPath(matrix))


# In[2]:


def test1():
    test = '''3\n7 4\n2 4 6\n8 5 9 3'''.replace('\n',',').split(',')
    test = [row.split(' ') for row in test]
    test = str2Int(test)
    assert findPath(test) == [3,7,4,9]
    
test1()


# In[ ]:




