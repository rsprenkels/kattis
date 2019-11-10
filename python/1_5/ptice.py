def ptice(correct_answers):
    answers = {'Adrian':"ABC" * 34, 'Bruno':"BABC" * 25, 'Goran':"CCAABB" * 20}
    score = {'Adrian':0, 'Bruno':0, 'Goran':0}

    for index, answer in enumerate(correct_answers):
        for boy in score:
            if answers[boy][index] == answer:
                score[boy] += 1

    max_score = max([score[boy] for boy in score])
    winners = [boy for boy in score if score[boy] == max_score]
    output = []
    output.append(f"{max_score}")
    for boy in winners:
        output.append(boy)
    return '\n'.join(output)


def test_ptice():
    assert ptice('AAAABBBBB') == """4
Adrian
Bruno
Goran"""

def test_2():
    assert ptice('BAACC') == """3
Bruno"""

if __name__ == '__main__':
    input()
    print(ptice(input()))