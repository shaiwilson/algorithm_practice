""" find rotation point """

def find_rotation_point(words):

    first_word = words[0]

    floor_index = 0
    ceiling_index = len(words) - 1

    while floor_index < ceiling_index:

        guess_index = floor_index + ((ceiling_index - floor_index) // 2)

        # if guess comes before first words

        if words[guess_index] > first_word:

            # go right
            floor_index = guess_index

        else:

            # go left
            ceiling_index = guess_index

        # if floor and ceiling have converged
        if floor_index + 1 == ceiling_index:
            return ceiling_index

def binary_search(lst, value):

    first = 0
    last = len(lst) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if lst[midpoint] == value:
            found = True
        else:
            if value < lst[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found