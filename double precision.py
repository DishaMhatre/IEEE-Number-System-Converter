# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 17:51:40 2020

@author: Admin
"""

import math
from decimal import Decimal

# STEP 1 : Convert the input number to binary

input_number = float(input("Please enter a decimal number: "))

if input_number > 0:
    sign_bit = 0
else:
    sign_bit = 1
    input_number = input_number * -1

"""
The given number can be a floating point value, and python bin() does not support fp, so we get floor of the fp value, and use
floor() on it. The decimal part is then converted separately.
"""

characteristic = int(math.floor(input_number))
binary_char = bin(characteristic)
binary = (binary_char[2:])

mantissa = input_number - characteristic
# For the sake of simplicity, we will calculate the binary version of mantissa upto a precision of 6 always.
# 0.4

mantissa_list = []
for i in range(0, 64):
    mantissa = 2 * mantissa
    mantissa_floor = int(math.floor(mantissa))
    mantissa_list.append(mantissa_floor)
    mantissa = mantissa - mantissa_floor

mantissa = (''.join(str(i) for i in mantissa_list))
# going to convert characteristic and mantissa to string and append
# them with a decimal in between, works better than using
# something like math.pow() [loss of precision]

binary_final = Decimal(binary + "." + mantissa)
# STEP 2 : Represent in scientific form / Calculate the bias factor

bias_factor = 1023 + len(binary) - 1

'''
IEEE Representation is 
SIGN + BIAS THINGY + REST OF SCIENTIFIC MANTISSA
'''

# signbit was calculated earlier

bias_y = bin(bias_factor)
sci_man = []

for i in range(1, len(binary)):
    sci_man.append(int(binary[i]))

rest_of_sci_man = 42 - len(binary)
for i in range(0, rest_of_sci_man + 1):
    sci_man.append(int(mantissa[i]))

final_ = str(sign_bit) + " " + bias_y[2:] + " " + ''.join(str(i) for i in sci_man)
print(final_)

