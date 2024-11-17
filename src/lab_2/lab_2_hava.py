import random

_array_length = 10
_random_min = -50
_random_max = 50
_array = []

def fill_array():
    for _ in range(_array_length):
        _array.append(random.randint(_random_min, _random_max))

    print("Source array %s" % _array)

def sort_array(array):
    _swapped = True
    _search_index = 0

    while _swapped:
        _swapped = False

        for _index in range(1, _array_length - _search_index):
            _previous_index = _index - 1

            if _array[_previous_index] > _array[_index]:
                swap(_previous_index, _index)
                _swapped = True

        _search_index += 1

    print("Result array %s" % _array)

def swap(_index_1, _index_2):
    _array[_index_1], _array[_index_2] = _array[_index_2], _array[_index_1]

if __name__ == '__main__':
    fill_array()
    sort_array(_array)