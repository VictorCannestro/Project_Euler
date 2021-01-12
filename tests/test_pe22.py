from src.pe22 import nameScore

def test_1():
    filename = 'data/p022_names.txt'

    # Open the file and read the contents
    with open(filename, 'r') as file:
        content = file.readlines()

    # Parse contents into a list of string names in alphabetical order
    names = sorted(content[0].upper().replace("\"",'').split(','))
    
    assert nameScore(names) == 871198282