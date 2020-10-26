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
############################################################################################################################

def sumOfSquares(n):
    return sum(i**2 for i in range(1,n+1))

def squareOfSum(n):
    return ((n*(n-1))//2)**2

n = 100
calc = squareOfSum(n) - sumOfSquares(n)
print(calc)
