def one_chicken(needed, provided):
    if needed > provided:
        if needed == provided + 1:
            plural = ''
        else:
            plural = 's'
        return f"Dr. Chaz needs {needed - provided} more piece{plural} of chicken!"
    else:
        if provided == needed + 1:
            plural = ''
        else:
            plural = 's'
        return f"Dr. Chaz will have {provided - needed} piece{plural} of chicken left over!"


def test_onechicken():
    assert one_chicken(20, 100) == 'Dr. Chaz will have 80 pieces of chicken left over!'

def test_2():
    assert one_chicken(10, 1) == 'Dr. Chaz needs 9 more pieces of chicken!'

if __name__ == '__main__':
    print(one_chicken(*list(map(int, input().split()))))