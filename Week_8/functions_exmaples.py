#-------------------------------------------------------------------------------
# Name:        Complex ArcPy Scripts and Generalizing Functions
# Purpose:      Chapter 4 of Toms
#
# Author:      Gregory Brunner
#
# Created:     28/01/2017
#-------------------------------------------------------------------------------

# Function  - A block of code that performs some action on data and returns the
#             result back to the code
#           - a.k.a. - subroutine or proceedure
#           - Designed to accept input data, transform it, and return it to the
#             main program

# Purpose of Functions - Avoid Repeating Code
#                      - Simplify programs

# A First Function
def firstFunction():
    'a simple function returning a string'
    return 'My first function'

firstFunction()

def secondFunction(number):
    'this function multiplies numbers by 3'
    return number * 3

def thirdFunction(number, multiplier=3):
    'this multiplies two numbers. If a second number is not specified, it '
    'multiplies the number by 3'
    if type(number) == type(1) or type(number) == type(1.0):
        return number * multiplier