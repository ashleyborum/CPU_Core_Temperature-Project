import numpy as np

class Matrices:

    def __init__(self, core_readings, num_rows):
        """
        Matrix class

        Args:
            num_rows: number of rows in file
        Yields:
            A matrix object
        """   
        self.x_matrix = create_matrix_X(num_rows)
        self.x_transpose = create_matrix_XT(num_rows)
        self.y_matrix = create_matrix_Y(core_readings)

#Construct Core Matrices
def create_matrix_X(num_rows):
    """
    Args:
        num_rows: number of rows in file
    Yields:
        An nx2 matrix, X, containing a column of 1's and a time 
        column in seconds incremented by 30 
    """
    time = np.zeros(num_rows)

    for i in range(0, num_rows):
        time[i] = i * 30

    c0 = np.ones(num_rows)
    c1 = time

    matrix_X = np.column_stack((c0, c1))

    return matrix_X

def create_matrix_Y(core_readings):
    """
    Args:
        core_readings: temperature readings from input file
    Yields:
        An nx1 matrix, Y, containing all temperature readings for each core
    """
    matrix_Y = np.array(core_readings)

    return matrix_Y

def create_matrix_XT(num_rows):
    """
    Args:
        num_rows: number of rows in file
    Yields:
        A 2xn matrix containing the transposed data from matrix_X
    """
    matrix_XT = create_matrix_X(num_rows).transpose()
   
    return matrix_XT