#!/usr/bin/env python

# version 1.1 02-November-2017

# Requires Future additions (http://www.python-future.org)
# Calculate speaker coverage based on driver dispersion angle and measured distance from source.

# Import Future functions
from __future__ import absolute_import, division, print_function, unicode_literals
from builtins import input
import math

title="Loudspeaker Coverage Calculator"
print(title)
print("=" * 80)

# Prompt for user input
cone_degrees = int(input("Enter speaker dispersion angle in degrees: "))
measured_distance = float(input("Enter measured distance from speaker in feet: "))

# Convert angles to radians
angle_radians = math.radians(cone_degrees)
radians_div = angle_radians / 2

# Calculate coverage pattern
coverage_pattern = ((math.tan(radians_div)) * measured_distance)* 2

# Round results to two decimal places
coverage_pattern_round = str(round(coverage_pattern, 2))

# Return results, prompt for user input to quit
print("Approximate speaker coverage pattern is: ", coverage_pattern_round, "ft.")
print()
print("Press the <Enter> key to exit.")
input()
