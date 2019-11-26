# https://open.kattis.com/problems/musicalscales

class ScaleLister():
    def __init__(self):
        self.notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
        self.scale_distances =  [2, 2, 1, 2, 2, 2, 1]

    def all_scales(self):
        for base_note in self.notes:
            index = self.notes.index(base_note)
            scale = [base_note]
            for note_number in range(len(self.scale_distances)):
                index += self.scale_distances[note_number]
                index = index % len(self.notes)
                scale.append(self.notes[index])
            yield scale

    def list_scales_for(self, song):
        possible_scales = []
        for scale in self.all_scales():
            if all(note in scale for note in song):
                possible_scales.append(scale[0])
        return sorted(possible_scales)

    def get_all_scales(self):
        return [scale for scale in self.all_scales()]


def test_1():
    song = ['C', 'D', 'F', 'D', 'C', 'D', 'F', 'F', 'F', 'C']
    assert ScaleLister().list_scales_for(song) == ['A#', 'C', 'D#', 'F']

def test_2():
    song = ['A', 'B', 'A', 'F#', 'G#', 'C']
    assert ScaleLister().list_scales_for(song) == []


def test_sorted_1():
    assert sorted(['D#', 'A#', 'C', 'F']) == ['A#', 'C', 'D#', 'F']


def test_allscales():
    assert ScaleLister().get_all_scales() == \
    [['A', 'B', 'C#', 'D', 'E', 'F#', 'G#', 'A'],
     ['A#', 'C', 'D', 'D#', 'F', 'G', 'A', 'A#'],
     ['B', 'C#', 'D#', 'E', 'F#', 'G#', 'A#', 'B'],
     ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C'],
     ['C#', 'D#', 'F', 'F#', 'G#', 'A#', 'C', 'C#'],
     ['D', 'E', 'F#', 'G', 'A', 'B', 'C#', 'D'],
     ['D#', 'F', 'G', 'G#', 'A#', 'C', 'D', 'D#'],
     ['E', 'F#', 'G#', 'A', 'B', 'C#', 'D#', 'E'],
     ['F', 'G', 'A', 'A#', 'C', 'D', 'E', 'F'],
     ['F#', 'G#', 'A#', 'B', 'C#', 'D#', 'F', 'F#'],
     ['G', 'A', 'B', 'C', 'D', 'E', 'F#', 'G'],
     ['G#', 'A#', 'C', 'C#', 'D#', 'F', 'G', 'G#']]

if __name__ == '__main__':
    _ = input()
    song = list(input().split())
    result = ScaleLister().list_scales_for(song)
    if len(result) > 0:
        print(' '.join(result))
    else:
        print('none')
