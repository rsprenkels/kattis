# https://open.kattis.com/problems/helpaphd

def help_a_phd(task):
    if task == 'P=NP':
        return 'skipped'
    else:
        a,b = list(map(int, task.split('+')))
        return str(a+b)


def test_helpaphd():
    assert help_a_phd('2+2') == '4'

def test_2():
    assert help_a_phd('P=NP') == 'skipped'

if __name__ == '__main__':
    num_cases = int(input())
    for case in range(num_cases):
        print(help_a_phd(input()))