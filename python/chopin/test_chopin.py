import sys


class Keyconverter():
    def __init__(self):
        self.unique_keys = set()
        for key in "ABCDEFG":
            self.unique_keys.add(key)
        self.alternate_keys = {}
        for alternate_pair in ['AB', 'CD', 'DE', 'FG', 'GA']:
            first: str = "{}#".format(alternate_pair[0])
            second: str = "{}b".format(alternate_pair[1])
            self.alternate_keys[first] = second
            self.alternate_keys[second] = first

    def lookup(self, key: str) -> str:
        parts = key.split(' ')
        if parts[0] in self.unique_keys:
            return 'UNIQUE'
        else:
            return self.alternate_keys[parts[0]] + ' ' + parts[1]


def chopin():
    case_counter: int = 0
    for line in sys.stdin:
        case_counter += 1
        print("Case {}: {}".format(case_counter, Keyconverter().lookup(line)))


def test_convert():
    assert Keyconverter().lookup('Ab minor') == 'G# minor'
    assert Keyconverter().lookup('G major') == 'UNIQUE'


if __name__ == '__main__':
    chopin()
