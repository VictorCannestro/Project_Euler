############################################################################################################################
#
# Problem 26
#
# 
#
# https://www.wikiwand.com/en/Repeating_decimal
# 
# Ans: 983
############################################################################################################################

def reduce_sample_space(d_threshold:int=1000) -> list:
    '''
    Parameters
    ----------
    d_threshold : int, optional
        The largest denominator of unit fraction 1/d to consider. The default 
        is 1000.
    Returns
    -------
    list
        Of d values where those resulting terminating decimals have been 
        filtered out.
    '''
    pass

def calculate_cycle_length(d: int) -> int:
    '''
    Parameters
    ----------
    d : int
        A natural number d > 0; the denominator of the unit fraction 1/d.
    Returns
    -------
    int
        The legnth of the repetend of unit fraction 1/d. Ranges from 0 to d-1.
    '''
    pass
    
def find_longest_repeating(d_threshold:int=1000) -> int:
    '''Returns the length of the longest repetend of 1/d that is found.'''
    return max(calculate_cycle_length(d) for d in range(1, d_threshold+1))      


if __name__ == '__main__':
    pass