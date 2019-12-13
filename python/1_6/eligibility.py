from datetime import datetime


def eleg_result(line):
    name, start_date, birth_date, courses = line.split()
    if datetime.strptime(start_date, '%Y/%m/%d').year >= 2010:
        return f"{name} eligible"
    elif datetime.strptime(birth_date, '%Y/%m/%d').year >= 1991:
        return f"{name} eligible"
    elif int(courses) >= 41:
        return f"{name} ineligible"
    else:
        return f"{name} coach petitions"


def eligibility(in_lines):
    return [eleg_result(line) for line in in_lines]


def test_1():
    in_lines = [
        'EligibleContestant 2013/09/01 1995/03/12 10',
        'IneligibleContestant 2009/09/01 1990/12/12 50',
        'PetitionContestant 2009/09/01 1990/12/12 35',
    ]
    assert eligibility(in_lines) == [
        'EligibleContestant eligible',
        'IneligibleContestant ineligible',
        'PetitionContestant coach petitions',
    ]


if __name__ == '__main__':
    print('\n'.join([eleg_result(input()) for _ in range(int(input()))]))
