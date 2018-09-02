from unittest.mock import patch

class Tarifa:
    def run(self) -> str:
        X: int = int(input())
        N: int = int(input())
        used: int = 0
        for i in range(N):
            used += int(input())
        return str((X * (N+1)) - used)

def test_1():
    problem = Tarifa()
    user_input = [
        '10','3','4','6','2'
    ]
    with patch('builtins.input', side_effect=user_input):
        assert problem.run() == '28'

# need to checkout
# https://dev.to/patrnk/how-to-test-input-processing-in-python-3

if __name__ == '__main__':
    print(Tarifa().run())
