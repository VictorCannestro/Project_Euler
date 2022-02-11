############################################################################################################################
#
# Problem 6
#
# The difference between the sum of the squares of the 
# first ten natural numbers and the square of the sum is 
# 3025 - 385 = 2640
#
# Find the difference between the sum of the squares of the 
# first one hundred natural numbers and the square of the sum.
#
# Ans: 25164150
############################################################################################################################

def sumOfSquares(n: int) -> int:
    '''Straightforward implementation using a generator'''
    return sum(i**2 for i in range(1, n+1))

def squareOfSum(n: int) -> int:
    '''Analytical formula for the sum of the frist n natrual numbers'''
    return ((n * (n + 1)) // 2) ** 2


if __name__ == "__main__":
    print(squareOfSum(100) - sumOfSquares(100))