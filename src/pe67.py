############################################################################################################################
#
# Problem 67
#
# Dev's note:
#
# This may not be correct. Suppose the "best choice" at the start
# leads to a chain of adjacent numbers that are less than if a sub-
# optimal point was choosen instead. So here, I'm really optimizing
# the path choices in a myopic way and might not find the global 
# solution depending on how the array is constructed.
#
############################################################################################################################

def str2Int(lst):
    '''Converts list of str to list of ints'''
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            lst[i][j] = int(lst[i][j])
    return lst

def findPath(matrix):
    '''
    Args:
        matrix: list of lists of ints
        
    Returns:
        The path of the yielding the maximum total from top
        to bottom of the triangle matrix input
    '''
    # set the initial starting point
    path = [matrix[0][0]]
    
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
        
    return path
                
    
with open('data/p067_triangle.txt') as file:
    tri = file.read()

matrix = tri.replace('\n',',').split(',')
matrix = [row.split(' ') for row in matrix]
matrix.pop(-1)
matrix = str2Int(matrix)
print(findPath(matrix))

# My answer:
# [59, 73, 52, 53, 87, 95, 90, 30, 84, 46, 56, 78, 45, 87, 51, 66, 76, 12, 70, 66, 89, 63, 
# 87, 79, 78, 61, 55, 98, 60, 77, 71, 99, 92, 49, 56, 89, 61, 68, 60, 94, 73, 44, 99, 92, 
# 77, 98, 67, 54, 68, 94, 64, 83, 50, 73, 44, 73, 80, 90, 87, 60, 64, 86, 93, 86, 64, 76, 
# 54, 30, 83, 42, 34, 69, 85, 67, 74, 92, 81, 78, 93, 88, 89, 60, 91, 91, 89, 91, 98, 87, 
# 52, 96, 96, 71, 51, 24, 11, 93, 60, 66, 85, 81]

def test1():
    test = '''3\n7 4\n2 4 6\n8 5 9 3'''.replace('\n',',').split(',')
    test = [row.split(' ') for row in test]
    test = str2Int(test)
    assert findPath(test) == [3,7,4,9]
    
test1()


