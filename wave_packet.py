#! /usr/bin/env python3

# Additional problem 1 of Assignment 6. (Not conplete yet)

import os
import numpy as np
import matplotlib.pyplot as plt

os.system("clear")

k0 = int(input("Enter the value of k0: "))
#width = float(input("Enter the width of packet on both side of k0 :"))
width = 1 # lower value will make the program faster
k_min = k0 - width
k_max = k0 + width
del_k = 0.01
gamma = .01 # To be choosed so that A is peaked

k_linspace = np.linspace(k_min, k_max, int(2 * width / del_k))

def amplitude(k_linspace, k0, gamma):

    amplitude_linspace = []
    for item in k_linspace:
        a = (( item - k0) ** 2 + gamma **2 ) ** -1
        amplitude_linspace.append(a)
    amplitude_linspace = np.array(amplitude_linspace)
    return amplitude_linspace

def w(k_linspace):

    w_linspace = []
    for item in k_linspace:
        w_linspace.append((item ** 2) / 2)
    w_linspace = np.array(w_linspace)
    return w_linspace


amplitude_linspace = amplitude(k_linspace, k0, gamma)
w_linspace = w(k_linspace)

def psi(x, t):

    global amplitude_linspace, w_linspace, k_linspace, del_k
    n = int(2 * width / del_k)
    psi_xt = 0
    for i in range(n):
        psi_xt += amplitude_linspace[i] * np.cos(-k_linspace[i] * x - w_linspace[i] * t)

    return psi_xt * del_k

number = int(input("Number of x points:"))
x_width = int(input("x width on each side of zero :"))

x_space  = np.linspace(-x_width,x_width,number)
psi_space = np.zeros(number)

"""plt.plot(k_linspace, amplitude_linspace)
plt.show()
"""
t = 0.1
while t == 0.1:
    print(t)
    for i in range(number):
        psi_space[i] = psi(x_space[i],t)

    plt.plot(x_space, psi_space)
    plt.show()

    t += 10
