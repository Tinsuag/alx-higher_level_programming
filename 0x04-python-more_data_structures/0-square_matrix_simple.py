#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """def square_cells(array):
        result = []
        for cell in array:
            print(cell)
            result.append(cell ** 2)
        return result
        """
    re = []
    for y in matrix:
        re.append(y**2)
        re = map(re, matrix)
    return re
