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
############################################################################################################################

# https://docs.python.org/3/library/string.html
import string

filename = '../data/p022_names.txt'

# Open the file and read the contents
with open(filename, 'r') as file:
    content = file.readlines()

# Parse contents into a list of string names in alphabetical order
names = sorted(content[0].upper().replace("\"",'').split(','))

# Give each name the value of its index + 1 in the sorted list
name_dict = {v:i+1 for i,v in enumerate(names)}

# Score the alphabet
alphabet = string.ascii_uppercase
scores = {v:i+1 for i,v in enumerate(alphabet)}

# For each name, sum the index value of each of its letters in the alphabet
scored_by_alpha = {key: sum(scores[letter] for letter in list(names[i])) for i, key in enumerate(name_dict)}

# Finally, multiply by its index to get the name score
scored_names = { k:scored_by_alpha[k]*name_dict[k] for k in scored_by_alpha.keys() }

print(sum(scored_names.values()))