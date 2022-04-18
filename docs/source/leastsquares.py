import numpy as np

def backsolve(matrix_XTX, matrix_XTY):
    """
    Solve system of equations using core matrices

    Per: Kennedy,T (2021) Numpy (Version 1.0)[Source code]. 
         https://github.com/cstkennedy/Python-Workshop/blob/master/NumPy/least_squares.py
    Args:
        matrix_XTX: a coefficient matrix which is an upper triangular matrix whose diagonal elements are not equal to zero
        matrix_XTY: a right-hand vector or constant matrix
    
    Yields:
        A solution vector when used within solve_matrix
    """
    
    num_rows, _ = matrix_XTX.shape

    for i in reversed(range(1, num_rows)):
        for j in reversed(range(0, i)):
            s = matrix_XTX[j, i]
            matrix_XTX[j, i] -= (s * matrix_XTX[i, i])
            matrix_XTY[j] -= (s * matrix_XTY[i])


def solve_matrix(matrix_XTX, matrix_XTY):
    """
    Solve a matrix

    Per: Kennedy,T (2021) Numpy (Version 1.0)[Source code]. 
         https://github.com/cstkennedy/Python-Workshop/blob/master/NumPy/least_squares.py
    Args:
        matrix_XTX: an upper triangular matrix whose diagonal elements are not equal to zero
        matrix_XTY: a right-hand vector

    Yields:
        A solution vector
    """

    num_rows, num_columms = matrix_XTX.shape

    for i in range(0, num_rows):
        # Find column with largest entry
        largest_idx = i
        current_col = i
        for j in range(i + 1, num_rows):

            if matrix_XTX[largest_idx, i] < matrix_XTX[j, current_col]:
                largest_idx = j

        # Swap
        if largest_idx != current_col:
            matrix_XTX[[i, largest_idx], :] = matrix_XTX[[largest_idx, i], :]
            matrix_XTY[[i, largest_idx]] = matrix_XTY[[largest_idx, i]]

        # Scale
        scaling_factor = matrix_XTX[i, i]
        matrix_XTX[i, :] /= scaling_factor
        matrix_XTY[i] /= scaling_factor

        # Eliminate
        for row_i in range(i + 1, num_rows):
            s = matrix_XTX[row_i][i]

            matrix_XTX[row_i] = matrix_XTX[row_i] - s * matrix_XTX[i]
            matrix_XTY[row_i] = matrix_XTY[row_i] - s * matrix_XTY[i]

    backsolve(matrix_XTX, matrix_XTY)


def least_squares_approx(matrix_object):
    """
    Compute coefficient values for _n_ CPU cores using least square approximation method

    Per: Kennedy,T (2021) Numpy (Version 1.0)[Source code]. 
         https://github.com/cstkennedy/Python-Workshop/blob/master/NumPy/least_squares.py
    Args:
        matrix_object: Matrix class to construct core matrix objects X, XT, and Y
    Yields:
        A vector containing coefficients c_0 and c_1 as floating point values
    """
    # Set up input for X, Y, and XT
    matrix_X = matrix_object.x_matrix
    matrix_XT = matrix_object.x_transpose
    matrix_Y = matrix_object.y_matrix

    # Compute XTX and XTY
    matrix_XTX = np.matmul(matrix_XT, matrix_X)
    matrix_XTY = np.matmul(matrix_XT, matrix_Y)

    solve_matrix(matrix_XTX, matrix_XTY)
    
    # Configure solved matrix
    config_matrix = np.zeros((1,2))
    config_matrix[0] = matrix_XTY
    
    return config_matrix