import sys


def savingdaylight(line: str) -> str:
    parts = line.split()
    start_hour, start_minute = map(int, parts[3].split(':'))
    end_hour, end_minute = map(int, parts[4].split(':'))
    diff_minutes = (end_hour * 60 + end_minute) - (start_hour * 60 + start_minute)
    result = ' '.join(parts[:3]) + f' {diff_minutes // 60} hours {diff_minutes % 60} minutes'
    return result

def test_1():
    assert savingdaylight('June 22 2005 6:24 20:37') == 'June 22 2005 14 hours 13 minutes'


for line in sys.stdin:
    print(savingdaylight(line))

# from 517.9 rank 680 (team 285.1 rank 132)