#
# codekata 2 - python, recursive (and ridiculous) approach
#

import random, math

#
# chop function
# 
# params:
# search_value: value to search for in array
# array:  array of positive integers (i'm assuming so, though codekata doesn't
# say "positive integers", otherwise -1 could be an element)
#
# returns:  array index of element, if element is found, or -1 if not
#
def chop(search_value, array):

    array_len = len(array)
    midpoint = math.ceil(array_len / 2)
    for array_index in range(0, midpoint):
        if array[array_index] == search_value:
            return array_index
    else:
        if midpoint == array_len:
            return -1
        else:
            chop_val = chop(search_value, array[midpoint:array_len])
            return chop_val if chop_val == -1 else midpoint + chop_val

if __name__ == "__main__":
    main()
