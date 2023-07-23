def solution(line: str) -> str:
    smiley = line.find(':)') > -1
    sad = line.find(':(') > -1
    if smiley and not sad:
        return 'alive'
    elif sad and not smiley:
        return 'undead'
    elif sad and smiley:
        return 'double agent'
    else:
        return 'machine'


def test_alive():
    assert solution('Hello, how are you? :)') == 'alive'


def test_undead():
    assert solution("Hey there! :( What's up? :(") == 'undead'


def test_double_agent():
    assert solution("::(Braaaains... are very useful for programming contests:))") == 'double agent'


def test_machine():
    assert solution("Firing up EmoticonBot... (:  : (  ):  :D  c:") == 'machine'

if __name__ == '__main__':
    print(solution(input()))