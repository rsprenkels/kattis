# https://open.kattis.com/problems/runlengthencodingrun

def rle(operation, message):
    if operation == 'E':
        output = ''
        while len(message) > 0:
            cur_group = message[0]
            group_len = 0
            while len(message) > 0 and message[0] == cur_group:
                group_len += 1
                message = message[1:]
            output += f"{cur_group}{group_len}"
        return output
    else:
        output = ''
        while len(message) > 0:
            output += message[0] * int(message[1])
            message = message[2:]
        return output


def test_1():
    assert rle('E', 'HHHeellloWooorrrrlld!!') == 'H3e2l3o1W1o3r4l2d1!2'


def test_2():
    assert rle('D', 'H3e2l3o1W1o3r4l2d1!2') == 'HHHeellloWooorrrrlld!!'


if __name__ == '__main__':
    print(rle(*input().split()))
