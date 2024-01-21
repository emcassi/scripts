#!/usr/bin/python

"""
Temperature Converter Script

This script allows the user to convert temperatures between Fahrenheit, Celsius, and Kelvin units.
The script accepts command-line arguments in the format:
    <input_temperature><input_unit> <output_unit>
For example: '32F C' to convert 32 Fahrenheit to Celsius.

Units:
    C - Celsius
    F - Fahrenheit
    K - Kelvin
"""

import sys

def is_valid_unit(unit):
    """ Check if the provided unit is valid (C, F, or K). """
    return unit in ["C", "F", "K"]

def convert_c_to_f(c):
    """ Convert Celsius to Fahrenheit. """
    return (c * 9/5) + 32

def convert_c_to_k(c):
    """ Convert Celsius to Kelvin. """
    return c + 273.15

def convert_f_to_c(f):
    """ Convert Fahrenheit to Celsius. """
    return (f - 32) * 5/9

def convert_f_to_k(f):
    """ Convert Fahrenheit to Kelvin. """
    return convert_c_to_k(convert_f_to_c(f))

def convert_k_to_c(k):
    """ Convert Kelvin to Celsius. """
    return k - 273.15

def convert_k_to_f(k):
    """ Convert Kelvin to Fahrenheit. """
    return convert_c_to_f(convert_k_to_c(k))

# Conversion dictionary
conversion_dict = {
    ("C", "F"): convert_c_to_f,
    ("C", "K"): convert_c_to_k,
    ("F", "C"): convert_f_to_c,
    ("F", "K"): convert_f_to_k,
    ("K", "C"): convert_k_to_c,
    ("K", "F"): convert_k_to_f,
}

def convert_temp(degrees, input_unit, output_unit):
    """ Convert temperature from one unit to another using the conversion dictionary. """
    try:
        conversion_func = conversion_dict[(input_unit, output_unit)]
        return conversion_func(degrees)
    except KeyError:
        print("Invalid conversion units")
        exit(1)

def format_answer(answer):
    """ Format the final answer to two decimal places or as an integer. """
    if answer == int(answer):
        return f"{int(answer)}"
    else:
        return f"{answer:.2f}"

if len(sys.argv) != 3:
    print("Usage: <input_temperature><input_unit> <output_unit>")
    exit(1)

input = sys.argv[1]
output = sys.argv[2]

degrees = 0
input_unit = input[-1].upper()
output_unit = output[0].upper()

try:
    degrees = float(input[:-1])
except ValueError:
    print("Invalid input Temperature")
    exit(1)

if not is_valid_unit(input_unit):
    print("Invalid Input Unit")
    exit(1)

if not is_valid_unit(output_unit):
    print("Invalid Output Unit")
    exit(1)

if input_unit == output_unit:
    print(input)
    exit(0)

answer = convert_temp(degrees, input_unit, output_unit)

print(f"{format_answer(answer)}°{output_unit}")
