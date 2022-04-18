# CPU Core Temperature Data
This project utilizes least squares approximation and linear interpolation to analyze the temperatures of four CPU cores over the course of a year. 

> The best way to crack a complex problem is to break it down into component parts, learn each of
the parts and learn how the parts go together. -Graham, R. L.

## Requirements
* Python
* Python3
* numpy

## Sample Execution and Output
Data takes the form of temperatures in a txt file. All data points are whitespace delimited.
```
python3 main.py sensors.txt
```
output *simliar* to
```
      0 <= x <      30; y_0      =      61.0000 +   0.6333x; interpolation
     30 <= x <      60; y_1      =      98.0000 +  -0.6000x; interpolation
     60 <= x <      90; y_2      =      20.0000 +   0.7000x; interpolation
     90 <= x <     120; y_3      =     128.0000 +  -0.5000x; interpolation
    120 <= x <     150; y_4      =      12.0000 +   0.4667x; interpolation
```
will  be displayed. Note that the form will vary by architecture/system.
