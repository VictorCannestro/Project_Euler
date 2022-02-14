############################################################################################################################
# Names scores
# Problem 22
# 
# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, 
# begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this 
# value by its alphabetical position in the list to obtain a name score.
#
# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 
# 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
#
# What is the total of all the name scores in the file?
#
# Ans: 871198282
############################################################################################################################

import string # https://docs.python.org/3/library/string.html


def nameScore(names: list) -> int:
    '''
    Parameters
    ----------
    names : list
        DESCRIPTION.
    Returns
    -------
    int
        The sum of all the name scores in the input. Names scores are found by
        working out the alphabetical value for each name and multipling this 
        value by its alphabetical position in the list to obtain a name score.
    '''
    alphabet = string.ascii_uppercase
    scores = {v:i+1 for i,v in enumerate(alphabet)} # Score the alphabet
    
    name_dict = {v:i+1 for i,v in enumerate(names)}                                      # Give each name the value of its index + 1 in the sorted list
    scored_by_alpha = {key: sum(scores[letter] for letter in list(names[i])) 
                                               for i, key in enumerate(name_dict)}       # For each name, sum the index value of each of its letters in the alphabet
    scored_names = { k:scored_by_alpha[k]*name_dict[k] for k in scored_by_alpha.keys() } # Finally, multiply by its index to get the name score
    return sum(scored_names.values()) 


def runCalculation(filename="../data/p022_names.txt"):
    '''Read in the names file and run the calculation'''
    with open(filename, 'r') as file:                              # Open the file and read the contents
        content = file.readlines()
    names = sorted(content[0].upper().replace("\"",'').split(',')) # Parse contents into a list of string names in alphabetical order
    print(nameScore(names))
    
    
if __name__ == "__main__":
    runCalculation()