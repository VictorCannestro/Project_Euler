############################################################################################################################
#
# Problem 18
#
# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum 
# total from top to bottom is 23.
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
# NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route.
#
# Ans: 1074
############################################################################################################################
from functools import lru_cache
from typing import List
import re 


def str2List(string: str) -> List[str]:
    '''
    Parameters
    ----------
    string : str
        A triangle of integers with rows separated by newlines.

    Returns
    -------
    cleaned : list
        Converts the triangle to nested list of strings representing integers.
        Example:
        >>s = '75\n    95 64\n    17 47 82'
        >>str2List(s)
        [['75'],['95','64'],['17','47','82']]
    '''
    temp = string.replace('\n',',')
    rgx = r" {2,}"
    temp = re.sub(rgx, '', temp).split(',')    
    cleaned = [row.split(' ') for row in temp]
    return cleaned


def str2IntElements(lst: List[str]) -> List[int]:
    '''Converts list of str to list of ints'''
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            lst[i][j] = int(lst[i][j])
    return lst


def findPathGreedy(matrix: List[List[int]]) -> List[int]:
    '''
    Parameters
    ----------
    matrix : List[List[int]]
        The tree of ints to consider. e.g. [[1], [3, 19], [32, 2, 45]]
    Returns
    -------
    List[int]
        The Greedy solution path yielding a maximum total from top to bottom 
        of the triangle matrix input. May NOT be the global maximum.
    '''
    path = [matrix[0][0]]                    # Set the initial starting points
    for i in range(1,len(matrix)):           # Iterate over each row in matrix, save for the first       
        idx = matrix[i-1].index(path[i-1])   # Record the index of the previous path max     
        valid_idxs = list(set([idx, idx+1])) # List indices of the adjacent elements        
        if valid_idxs[-1] >= len(matrix[i]): # If a candidate is outside the bounds, drop it
            valid_idxs.pop(-1)   
        choices = []
        for k in valid_idxs:       
            choices.append(matrix[i][k])     # Record values of the 2-3 candidates  
        v = max(choices)                     # Select the largest path element candidate
        path.append(v)
    return path


def _A179477(n: int) -> int:
    '''
    Parameters
    ----------
    n : int
        Must be that n >= -1. 
    Returns
    -------
    int
        Generates the corresponding term in sequence A179477: 1, 10, 99, 988, 9877, ...
    '''
    return (10 + 2**(5+n) * 5**(2+n) + 9*n) // 81

@lru_cache()
def _diffPattern(N: int) -> List[int]:
    '''
    Parameters
    ----------
    N : int
        Must be that n >= 2.
    Returns
    -------
    List[int]
        Returns a list of the differences between subsequent terms of the indices
        of valid traversals of elements in the tree:       
                                  a        [[a],
                                 b c        [b,c], 
                                d e f       [d,e,f]
                                 ...          ...  ]     
        For example if N=3, then the valid paths and their list of indices would be: 
                  a->b->d            [[0,0,0],       
                  a->b->e             [0,0,1], 
                  a->c->e             [0,1,1], 
                  a->c->f             [0,1,2]]
        and the differences between those lists taken as whole numbers would 
        be [1, 10, 1]. For N=4 it would be [1, 10, 1, 99, 1, 10, 1], and so on.
    '''
    if N < 2:
        raise ValueError("It must be that N >= 2")
    elif N == 2:
        return [_A179477(-1)]
    else:
        return _diffPattern(N-1) + [_A179477(N-3)] + _diffPattern(N-1) 
   
def _list2int(array: List[int]) -> int:
    '''E.g. _list2int([1,2,3,4]) returns 1234''' 
    num = ''
    for item in array:
        num += str(item)
    return int(num)

def _int2list(num: int) -> List[int]:
    '''E.g. _int2list(12345678910) returns [1,2,3,4,5,6,7,8,9,10]'''
    preprocessed = list(str(num))          # e.g. ['9','1','0','1','1']
    postprocessed = [int(preprocessed[0])] # e.g. [9]
    i, k = 1, 1
    while i < len(preprocessed):
        if postprocessed[-1] == 9 and preprocessed[i:i+k+1] == ['1','0']: # If we transition to 2 digits
            k = 2                                                         # Slice every 2 digits 
        if k == 1:
            sliced = [int(preprocessed[i:i+k][0])]
        else:
            a,b = preprocessed[i:i+k]
            sliced = [int(a)*10 + int(b)]
            i += 1
        postprocessed += sliced 
        i += 1
    return postprocessed

# The problem is traced to here for adding transitions of 2 digit integers
def _transition(old_path, difference)-> List[int]: 
    converted = _list2int(old_path) + difference
    print(converted)
    padding = len(old_path) - len(str(converted))
    return [0]*padding + _int2list(converted) # Might need adjustment

def bruteForce(tree: List[List[int]]) -> int:
    '''
    Parameters
    ----------
    tree : List[List[int]]
        The tree of ints to consider. e.g. [[1], [3, 19], [32, 2, 45]].
    Returns
    -------
    int
        The sum of the path that generates the maximal sum, out of all 2**(n-1) paths.
    '''
    length = len(tree)
    differences = _diffPattern(length)         # Precompute the difference pattern
    idx_paths = [[0 for k in range(length)]]   # Initialize the zero path
    for i in range(1, len(differences) + 1):   # Iterate 2**(n-1) - 1 times
        idx_paths.append(_transition(idx_paths[i-1], differences[i-1]))
    paths = [list(map(lambda row, idx: row[idx], tree, idx_paths[i])) for i in range(len(idx_paths))] # Map from the idx_paths to the corresponding path of tree values
    return max(sum(path) for path in paths)
    

def findPathDynamic(matrix: List[List[int]]) -> List[int]:
    '''
    Parameters
    ----------
    matrix : List[List[int]]
        The tree of ints to consider. e.g. [[1], [3, 19], [32, 2, 45]].
    Returns
    -------
    List[int]
        The Dynamic Programming solution to find the path that maximizes the 
        sum of the elements traversed.
    '''
    pass
    
                 
if __name__ == "__main__":
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
    print(bruteForce(str2IntElements(str2List(tri))))