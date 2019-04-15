#!python


def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text.
    Run time: """
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement contains here (iteratively and/or recursively)
    
    
    index = find_index(text, pattern) # find_index() function is O(n*m)
    
    if index != None: # O(1)
        return True
    return False


def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found. This is more C++ way of checking the chars in the string
    Run time: O(n*m), n is length of the string,"""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    
    if pattern == "":
        return 0
    
    starter = 0 # the starting index of the patterin in the text
    index = 0 # index for text
    subindex = 0 # index for pattern 


    while index <= len(text) - 1:

        if text[index] == pattern[subindex]:
            index += 1
            subindex +=1

            if subindex == len(pattern): # check for if we checked all index of patter  
                # starter index of the text where pattern occured 1st time
                return starter  

        else: # mismatch found 
            starter += 1 # shift the starter to next index
            index = starter 
            subindex = 0 # reset the subindex 
        
    return None


def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    if pattern == '':  # all strings contain empty string
        # and creae a list with the number of items equals to length of the text
        return list(range(len(text))) 

    
    # get the first occurance of the pattern in the text to cut the running time 
    index = find_index(text, pattern)
    
    indexes = []
    
    if index != None: # pattern occured in the text so we can check if there are more
        indexes.append(index)

        index = index + 1 # check for the char 1 next to the index 
        starter = index  # starting the new window
        subindex = 0  # index for pattern

        while index <= len(text) - 1:
            if text[index] == pattern[subindex]:
                index += 1
                subindex += 1
                
                if subindex == len(pattern):  # found another occurance of the pattern
                    
                    indexes.append(starter)
                    subindex = 0 # reset the subindex
                    starter += 1 # 
                    index = starter

            else:  # mismatch found
                subindex = 0  # reset the subindex
                starter += 1  # shift the starter to next index
                index = starter
    
        return indexes # all occured list of indexes 
    
    return  indexes # not found return empty list
    


def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
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
    