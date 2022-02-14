############################################################################################################################
#
# Probelm 16
#
# 2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2**1000?

# We could use the fact that 990 / 15 = 66 with the result that
# 2**15 = 32768, then multiply by the last 2**10 to get the 
# answer, however python seems to be able to do this directly.
#
# Ans: 1366
############################################################################################################################

def sum_digits(n: int) -> int:
    '''
    Args:
        n (int): the number whose digits we'll sum
    Return:
         (int): the sum of the digits of the input
    '''
    return sum(int(digit) for digit in str(n))


if __name__ == "__main__":
    print(sum_digits(2**1000))
