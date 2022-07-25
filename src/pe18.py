'''
Problem 18

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum 
total from top to bottom is 23.

               3
              7 4
             2 4 6
            8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. 
WHY 16384? Because with only 1 row there is 1 choice; 2 rows = 2 choices; 3 rows = 4 choices;
           4 rows = 8 choices, etc. So the Nth row has 2**(N-1) path choices. 

Ans: 1074
'''
from typing import List
import numpy as np
import re 

Tree = List[List[int]]


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
   
def generateIndicesOfPaths(n: int) -> list:
    '''
    Parameters
    ----------
    n : int
        The number of rows (i.e. the depth) of the tree.

    Returns
    -------
    A : np.array
        A 2**(n-1) length array of the indices of valid paths in the tree. Uses
        the insight that the valid paths of the N-1 lenth tree can be used to 
        generate those in the Nth lenth tree via block matrices. 
    '''
    A = np.array([[0]])
    for n in range(1, n):
        ones = np.ones_like(A)
        zeros = np.zeros(((2*len(A), 1)))
        A = np.concatenate((A, A + ones), axis=0)
        A = np.concatenate((zeros, A), axis=1)
    return A.astype(int).tolist()
    
def bruteForce(tree: Tree) -> int:
    '''
    Parameters
    ----------
    tree : Tree 
        A list of lists of integers in which the first nested list has 1 element,
        the second has 2 elements, etc.

    Returns
    -------
    int
        The global maximum path sum of the given tree input.
    '''
    indices_of_paths = generateIndicesOfPaths(len(tree))
    paths = [[tree[k][v] for k,v in enumerate(idx_path)] for idx_path in indices_of_paths]
    return max(sum(path) for path in paths)


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