from src.pe22 import nameScore, runCalculation


class TestNameScore(object):
    def test_answer(self):
        filename = 'data/p022_names.txt'
        with open(filename, 'r') as file:
            content = file.readlines()
        names = sorted(content[0].upper().replace("\"",'').split(','))
        calc = nameScore(names)
        ans = 871198282
        message = f"Expected {ans}\nBut got {calc}"
        assert calc == ans, message 
        

class TestRunCalculation(object):
    '''https://docs.pytest.org/en/6.2.x/capture.html'''
    def test_answer(self, capsys):
        runCalculation('data/p022_names.txt')
        captured = int(capsys.readouterr().out)
        ans = 871198282
        message = f"Expected {ans}\nBut got {captured}"        
        assert captured == ans, message