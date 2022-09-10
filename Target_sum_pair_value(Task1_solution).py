def get_aspected_index(two_pair_values, target_value):
    
    for i in range(len(two_pair_values[0]) - 1):

        # start from the i'th element until the last element
        for j in range(i + 1, len(two_pair_values[0])):

            # if the desired sum is found, print it
            if two_pair_values[0][i] + two_pair_values[0][j] == target_value:
                print(two_pair_values.index(two_pair_values[0]))


    for i in range(len(two_pair_values[1]) - 1):

        # start from the i'th element until the last element
        for j in range(i + 1, len(two_pair_values[1])):

            # if the desired sum is found, print it
            if two_pair_values[1][i] + two_pair_values[1][j] == target_value:
                print(two_pair_values.index(two_pair_values[1]))


    for i in range(len(two_pair_values[2]) - 1):

        # start from the i'th element until the last element
        for j in range(i + 1, len(two_pair_values[2])):

            # if the desired sum is found, print it
            if two_pair_values[2][i] + two_pair_values[2][j] == target_value:
                print(two_pair_values.index(two_pair_values[2]))


    for i in range(len(two_pair_values[3]) - 1):

        # start from the i'th element until the last element
        for j in range(i + 1, len(two_pair_values[3])):

            # if the desired sum is found, print it
            if two_pair_values[3][i] + two_pair_values[3][j] == target_value:
                print(two_pair_values.index(two_pair_values[3]))


    for i in range(len(two_pair_values[4]) - 1):

        # start from the i'th element until the last element
        for j in range(i + 1, len(two_pair_values[4])):

            # if the desired sum is found, print it
            if two_pair_values[4][i] + two_pair_values[4][j] == target_value:
                print(two_pair_values.index(two_pair_values[4]))


    for i in range(len(two_pair_values[5]) - 1):

        # start from the i'th element until the last element
        for j in range(i + 1, len(two_pair_values[5])):

            # if the desired sum is found, print it
            if two_pair_values[5][i] + two_pair_values[5][j] == target_value:
                print(two_pair_values.index(two_pair_values[5]))


    for i in range(len(two_pair_values[6]) - 1):

        # start from the i'th element until the last element
        for j in range(i + 1, len(two_pair_values[6])):

            # if the desired sum is found, print it
            if two_pair_values[6][i] + two_pair_values[6][j] == target_value:
                print(two_pair_values.index(two_pair_values[6]))


    for i in range(len(two_pair_values[7]) - 1):

        # start from the i'th element until the last element
        for j in range(i + 1, len(two_pair_values[7])):

            # if the desired sum is found, print it
            if two_pair_values[7][i] + two_pair_values[7][j] == target_value:
                print(two_pair_values.index(two_pair_values[7]))


if __name__ == '__main__':
    two_pair_values = [[1, 5], [9, -7], [0, 8], [6, 3], [4, 11], [14, 0], [8, 1], [4, 9]]
    target_value = 9
    get_aspected_index(two_pair_values, target_value)



    
