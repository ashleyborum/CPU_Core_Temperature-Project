import numpy as np

def interpolate(matrix_object):
    """
    Compute coefficient values for a line for _n_ CPU cores using linear 
    interpolation method

    Args:
        matrix_object: Matrix class to construct core matrix objects X and Y
    Yields:
        A List containing coefficients c_0 and c_1 as floating point values
    """
    X = np.hsplit(matrix_object.x_matrix, 2)
    Y = matrix_object.y_matrix
   
    n = len(Y)
    X = X[1].reshape(n, 1)

    c_i = np.zeros((n-1, 2))

    for k in range(1, n+1):
        for i in range(0, n-k):
            #m, slope of line
            c_1 = (Y[i+1] - Y[i]) / (X[i+1] - X[i])
            c_i[i][1] = c_1

            #b, intercept of line
            c_0 = Y[i] - (c_1 * X[i])  
            c_i[i][0] = c_0

    return c_i