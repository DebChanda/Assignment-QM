#! /usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

LOWER_X = -5
UPPER_X = -LOWER_X

def fact(num):
    dummy = 1
    factorial = 1
    while dummy <= num:
        factorial *= dummy
        dummy += 1
    return factorial


def hermite_gen(x_value, order):

    h0 = 1
    h1 = 2 * x_value
    n = 2
    hermite_values = [h0, h1]
#    hermite_values.append(h0,h1)
    while n <= order:
        hermite = 2 * x_value * hermite_values[n - 1] - 2 * (n - 1) * hermite_values[n - 2]
        hermite_values.append(hermite)
        n += 1

    return hermite_values[order]


# order = int(input("Order of Polynomial  : "))
# print("Answer ", fact(order))

def wavefunc(order):

    x_data = np.linspace(LOWER_X,UPPER_X,1000)
    psi_data = []
    const = 1 / (2 ** order * fact(order) * np.pi ** 0.5) ** 0.5
    for data in x_data:
        psi = const * np.exp(- data ** 2 / 2) * hermite_gen(data, order)
        psi_data.append(psi)

    return x_data, psi_data

order = int(input("Order of WaveFunction  : "))
for x in range(0, order + 1):

    x_data, psi_data = wavefunc(x)
    plt.plot(x_data, psi_data, label = "WaveFunc at state " + str(x))

potential_data = []
for data in x_data:
    potential_data.append(.1 * data ** 2)
plt.plot(x_data, potential_data, label = "Potential")
plt.legend()
plt.show()
