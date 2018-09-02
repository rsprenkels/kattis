from unittest.mock import patch
import filip

def test_1():
    myBoy = filip.filip()
    user_input = [
        '734 893'
    ]
    with patch('builtins.input', side_effect=user_input):        
        assert myBoy.giveLargest() == '437'

# need to checkout 
# https://dev.to/patrnk/how-to-test-input-processing-in-python-3
