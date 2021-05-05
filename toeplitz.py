# checks if a matrix is a toeplitz matrix
# should have numbers repeating diagonally down-right

import numpy as np

def isToeplitz(arr):
    """
    @param arr: int[][]
    @return: bool
    """
    # in case input is a list
    arr = np.array(arr)

    # will iterate over rows to check toeplitzness
    rows, cols = arr.shape

    # each row should be the same as the row above it but one element different
    # [1,2,3,4]
    # [5,1,2,3]
    # so we'll check all rows (but the last which has nothing below it)
    for row in range(rows-1):
      # all but the last
      top = arr[row][:-1]

      # all but the first
      bottom = arr[row+1][1:]

      # these should be the same
      if not np.array_equal(top, bottom):
        return False

    # if none were ever different then it's a toeplitz
    return True