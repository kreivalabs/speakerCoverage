#!/usr/bin/env python
#requires Future additions (http://www.python-future.org)
#Calculate speaker coverage based on driver dispersion angle and measured distance from source.

#import Future functions
from __future__ import absolute_import, division, print_function, unicode_literals
from builtins import input
import math

#prompt for user input
cone_degrees = int(input("Enter speaker dispersion angle in degrees: "))
measured_distance = float(input("Enter measured distance from speaker in feet: "))

#convert angles to radians
angle_radians = math.radians(cone_degrees)
radians_div = angle_radians / 2

#calculate coverage pattern
coverage_pattern = ((math.tan(radians_div)) * measured_distance)* 2

#display results, prompt for user input to quit.
print('Speaker coverage pattern is: ', coverage_pattern, 'ft.')
print('Press the <Enter> key to exit.')
input()
