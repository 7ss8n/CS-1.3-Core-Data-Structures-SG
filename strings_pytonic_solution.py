#!python


def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement contains here (iteratively and/or recursively)

    index = find_index(text, pattern)

    if index != None:
        return True
    return False

def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_index here (iteratively and/or recursively)

    window = len(pattern)

    if len(pattern) == 0:
        return 0

    else:
        index = 0
        # change the wile loop to for loop bc we know the number of iterations
        # greater or equals to catch the patter if it's last index
        while index <= len(text) - 1:
            # running time is "n" iterations => O(n*m) is total runnning time
            if pattern == text[index : window + index]:
                # C++ way checking the index is faster and save up the memory and copying the string slice
                # this is going to be O(m) if the pattern is big like paragraph
                # and uses more memory O(m)
                return index
            index += 1

    return None


def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)


    # instead of starting at 0, I can start where i found patter and start at the index + 1
    index = 0
    window = len(pattern)
    indexes = []

    if pattern == '':
        # for empty pattern creates list of indecies of the text
        return list(range(len(text)))

    else:
        # greater or equals to catch the patter if it's last index
        while index <= len(text) - 1:
            if pattern == text[index:window + index]:
                indexes.append(index)
            index += 1

    return indexes

def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    # main()
    # indexes1 = find_all_indexes('abcabcabc', 'abc')
    # print("result => [0, 3, 6]: ", indexes1)
    indexes2 = find_all_indexes('abcabcdabcde', 'abcd')
    print("indexes2 => [3, 7]: ", indexes2)
