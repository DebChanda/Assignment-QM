#! /usr/bin/env python3

# Additional problem 1 of Assignment 6. (Nogit addt conplete yet)

import os
import numpy as np
import matplotlib.pyplot as plt

os.system("clear")

k0 = int(input("Enter the value of k0: "))
width = 1 # lower value will make the program faster
k_min = k0 - width
k_max = k0 + width
del_k = 0.01
gamma = 0.01 # To be choosed so that A is peaked

k_linspace = np.linspace(k_min, k_max, int(2 * width / del_k))

def generator(k_linspace):

    global k0, gamma

    amplitude_linspace = 1 / (( k_linspace - k0) ** 2 + gamma **2 )
    w_linspace = k_linspace ** 2/2

    return amplitude_linspace, w_linspace

amplitude_linspace, w_linspace = generator(k_linspace)

def psi(x, t):

    global amplitude_linspace, w_linspace, k_linspace, del_k
    n = int(2 * width / del_k)
    psi_xt = 0
    for i in range(n):
        psi_xt += del_k * amplitude_linspace[i] * np.cos(k_linspace[i] * x - w_linspace[i] * t)

    return psi_xt

if input("Enter y/n :") == "y":
    number = int(input("Number of x points:"))
    x_width = int(input("x width on each side of zero :"))
else:
    number = 900
    x_width = 300

x_space  = np.linspace(-x_width,x_width,number)


#plt.plot(k_linspace, amplitude_linspace)
#plt.show()

t = 0
ON = True
while ON:
    psi_space = psi(x_space, t)

    plt.plot(x_space, psi_space,label = "At time : {}".format(t), zorder = 1)
    plt.plot(x_space, np.zeros(number), "k-", label = "x-axis", zorder = 2)
    plt.scatter([k0 * t],[0],color = "r", s = 100, label = "Classical Partcle", zorder = 3)
    print([k0 * t],[0])
    plt.legend()
    plt.show()

    t += 10
    if t >= 30:
        ON = False
