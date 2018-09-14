#! /usr/bin/env /home/debc/Env/mkh/bin/python3

# Additional problem 1 of Assignment 6.
import os
import numpy as np
import matplotlib.pyplot as plt

os.system("clear")

k0 = int(input("Enter the value of k0 (< 10 for better graph): "))
width = 0.5  # lower value will make the program faster
k_min = k0 - width
k_max = k0 + width
del_k = 0.01
gamma = 0.01  # To be choosed so that A is peaked

k_linspace = np.linspace(k_min, k_max, int(2 * width / del_k))


def generator(k_linspace):

    global k0, gamma
    amplitude_linspace = 1 / ((k_linspace - k0) ** 2 + gamma ** 2)
    w_linspace = k_linspace ** 2 / 2

    return amplitude_linspace, w_linspace


amplitude_linspace, w_linspace = generator(k_linspace)


def psis(x_space, t):

    global amplitude_linspace, w_linspace, k_linspace, del_k
    psi_space = []
    psimod_space = []
    for x in x_space:
        data = (del_k * amplitude_linspace * np.exp(0 + 1j *
                                                    (k_linspace * x - w_linspace * t))).sum()
        psimod_space.append(abs(data))
        psi_space.append(data.real)
    return psimod_space, psi_space


if input("Wanna change the dafault range of x (-500 to +500)(y/n) :") == "y":
    number = int(input("Number of x points:"))
    x_width = int(input("x width on each side of zero :"))
else:
    number = 1500
    x_width = 500

x_space = np.linspace(-x_width, x_width, number)

t = 0
ON = True
while ON:
    psimod_space, psi_space = psis(x_space, t)

    plt.title("Plot for k0 = {}".format(k0))

    plt.plot(x_space, psi_space, label="Psi at time : {}".format(t), zorder=1)
    plt.plot(x_space, psimod_space, "g--",
             label="|Psi| at time : {}".format(t), zorder=2)
    plt.plot(x_space, np.zeros(number), "k-", label="x-axis", zorder=3)
    plt.scatter([k0 * t], [0], color="r", s=100,
                label="Classical Partcle", zorder=4)

    plt.xlabel("x")
    plt.ylabel("Psi(x) and |Psi(x)|")

    plt.legend()
    plt.show()

    t += 10
    if t >= 50:
        ON = False
