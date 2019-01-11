import binary_search, random

def test_chop():

    # One element, in
    array = [5]
    search_value = 5
    assert(binary_search.chop(search_value, array) == 0)

    # One element, not
    search_value = 6
    assert(binary_search.chop(search_value, array) == -1)

    # Two, in
    array = [0, 1]
    search_value = 1
    assert(binary_search.chop(search_value, array) == 1)

    # Two not
    array = [0, 1]
    search_value = 2
    assert(binary_search.chop(search_value, array) == -1)

    total_iterations = 100
    max_array_size = 1000

    for test_iteration in range(1, total_iterations + 1):

        array = []

        num_elements = random.randint(1, max_array_size + 1)
        for element_add in range(0, num_elements):
            array.append(random.randint(1, num_elements + 1))
        array.sort()

        search_value = random.randint(1, num_elements + 1)

        search_result = binary_search.chop(search_value, array)
        if search_result is -1:
            found = True
            try:
                array.index(search_value)
            except ValueError as err:
                found = False
            assert(not found)
        else:
            assert(array[search_result] == search_value)
