#! /usr/bin/env python3

## Solution of question number 2 of Ass 6.

#import matplotlib.pyplot as plt
import scipy.special as sp , os

os.system("clear")
n = int(input("Enter the number of energy states to find :"))
l = float(input("Enter the scaled value of length : "))

i = 1
energy = 0
energy_in = 0.01
value = value_prev = 0
while i <= n:
    x = - (2**(1/3)) * (energy)
    y =  (2**(1/3)) * (-energy + l)
    airy_values = sp.airy(x)
    airy_values2 = sp.airy(y)
    value = airy_values[0] * airy_values2[1] - airy_values[1] * airy_values2[0]
    if value * value_prev < 0:
        # We have a Solution
        print("For state {}, scaled energy is : {:.3f}".format(i, energy), value_prev, value)
        i += 1

    value_prev = value
    energy += energy_in
