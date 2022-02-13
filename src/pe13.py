##########################################################################################
# 
# Problem 13
#
# Work out the first ten digits of the sum of the following one-hundred, 50-digit numbers.
#
# Ans: 5537376230
##########################################################################################
from typing import List


def read_data(filename: str="../data/p013_50-digit_ints.txt"):
    '''Attempts to read in the passed filename and returns its contents'''
    with open(filename) as blob:
        return blob.readlines()
        
def clean(text: List[str]) -> List[int]:
    '''Utility function to strip newlines and cast elements to ints'''
    return [int(num.replace('\n','')) for num in text] 

def take_first_n_digits(n: int, cleaned_blob: List[int]) -> int:
    '''Returns the first ten digits of the sum of the cleaned_blob'''
    big_num = str(sum(cleaned_blob))
    if n > len(big_num):    # If requested digits are out of range, use length
        return int(big_num)
    return int(big_num[:n]) # Slice first n digits, then cast back to an int


if __name__ == "__main__":
    print(take_first_n_digits(10, clean(read_data())))