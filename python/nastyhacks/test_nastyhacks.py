from unittest.mock import patch

def nastyhacks():
    
def test_nastyhacks(capsys):
    input = [
        '3',
        '0 100 70',
        '100 130 30',
        '-100 -70 40'
    ]
    with patch("builtins.input", side_effect=input):
        nastyhacks()
    out, err = capsys.readouterr()
    assert out.split('\n')[:-1] == [
        'advertise',
        'does not matter',  
        'do not advertise']

