from src.pe13 import cleaned

def test_1():
    blob = '''1234
    1234
    1234
    1234'''
    assert len(cleaned(blob)) == 4