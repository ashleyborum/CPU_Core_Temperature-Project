import sys
import numpy as np
from pre_process import Matrices
from linear_interpolation import interpolate
from leastsquares import least_squares_approx
from parse_temps import (parse_raw_temps)
from output import (output_to_file)


def main():
    """
    This program implements the piecewise linear interpolation and
    least squares methods to analyze CPU core temperature data. 

    Args:
        An input filename given as the first command line argument
    Yields:
        A .txt file (one file per core) containing lines of output 
        of the form: x_k <= x < x_k+1; y_i = c_0 + c_1x; type
    """
    if len(sys.argv) < 2:
        print("No input file provided.")
        print("Usage: {:} input_file".format(*sys.argv))
        exit(1)

    readings_filename  = sys.argv[1]

    time = []
    readings_core_0 = []
    readings_core_1 = []
    readings_core_2 = []
    readings_core_3 = []

    num_lines = 0 
    
    core_readings = [readings_core_0, readings_core_1, readings_core_2, readings_core_3]

    with open(readings_filename, 'r') as core_readings_in:
        for time_step, core_temps in parse_raw_temps(core_readings_in):
            time.append(time_step) 
            readings_core_0.append(core_temps[0])
            readings_core_1.append(core_temps[1])
            readings_core_2.append(core_temps[2])
            readings_core_3.append(core_temps[3])
            num_lines += 1

    for core in range(4):
        new_matrix = Matrices(core_readings[core], num_lines)
        interpolation = interpolate(new_matrix)
        least_squares = least_squares_approx(new_matrix)
        output_to_file(interpolation, least_squares, core)
    
if __name__ == "__main__":
    try:
        main()
    except FileNotFoundError as err:
        print(err)