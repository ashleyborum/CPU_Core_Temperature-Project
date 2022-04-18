def output_to_file(interpolation_vals, approx_vals, core_num):
    """
    Prints output data to files

    Args:
        interpolation_vals: coefficient values returned by interpolation module 
        approx_vals: coefficient values returned by least squares approximation module
        core_num: index of core to be output
    Yields:
        A .txt file containing computed least squares and interpolation data for each of _n_ cores
    """
    output_filename = "interpolation-core-" + str(core_num) + ".txt"
    count = 0

    with open(output_filename, 'w') as out:
        for vals in interpolation_vals:
            out.write("{start:>12}{stop:>9}; {y:<10}={c0:>14} +{c1:>10}; {i}".format(start = str(count * 30) + " <= x <", 
                                                                                     stop  = str(count * 30 + 30),
                                                                                     y     = "y_" + str(count), 
                                                                                     c0    = f"{vals[0]:.4f}", 
                                                                                     c1    = f"{vals[1]:.4f}" + "x", 
                                                                                     i     = "interpolation" + '\n'))
            count += 1
        for vals2 in approx_vals:
            out.write("{start:>12}{stop:>9}; {y:<10}={c0:>14} +{c1:>10}; {a}".format(start = str(count * 0) + " <= x <", 
                                                                                     stop  = str(count * 0 + 30),
                                                                                     y     = "y_" + str(count), 
                                                                                     c0    = f"{vals2[0]:.4f}", 
                                                                                     c1    = f"{vals2[1]:.4f}" + "x", 
                                                                                     a     = "least-squares"))


        out.close()