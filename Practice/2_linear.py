import matplotlib.pyplot as plt
import numpy as np

energy = 0.0
energy_increase = 0.01
total = 1000
meet = int(0.6 * total)

x = np.linspace(-6,6, total)
dx = x[1] -x[0]

def potential(x):
    V = abs(x)
    return V


def solution(psi_old, psi1_old, psi2_old, data):
    
    # Rescaling the wave function
    scale = 1 / psi_old[meet] * data

    for i in range(meet, total):
        psi_old[i] = psi_old[i] * scale
        psi1_old[i] = psi1_old[i] * scale
        psi2_old[i] = psi2_old[i] * scale


    # Normalizing the wave function

    A = (sum(psi_old**2) * dx) ** 0.5
    psi_old = psi_old/A
    psi1_old /= A
    psi2_old /= A

    if (input("Show graphs?(y/N):") == 'y'):

        plt.style.use('ggplot')
        plt.title("Wave function for energy eigenstate {}".format(found - 1))
        plt.plot(x,np.zeros(total),"k--",alpha = 0.5)
        plt.plot(np.zeros(total),np.linspace(psi_old.min(),psi_old.max(),total),"k--",alpha = 0.5)
        plt.plot(x,psi_old,label = "Energy = {:.2f}".format(energy - energy_increase))
        # plt.plot(x,psi1_old,label = "Psi1")

        plt.legend()
        plt.show()

    p2_avg = -sum(psi2_old * psi_old ) * dx
    v_avg = sum(psi_old * psi_old * V) * dx

    # Showing the result
    print("Energy of energy eigenstate {} = {:.2f}".format(found - 1,energy - energy_increase))
    print("Average of potential = {:.2f}".format(v_avg))
    print("Average of square of momentum = {:.2f}".format(p2_avg))
    
    return 0


# Initializing the Wave Functions

psi = np.zeros(total)
psi1 = np.zeros(total)
psi2 = np.zeros(total)

psi_old = np.zeros(total)
psi1_old = np.zeros(total)
psi2_old = np.zeros(total)

# No. of states to find

n = 3
found = 0
k_p = 0
k_pp = 0
data1bak = 0
databak  = 0

# Loop to brute force through energy values in steps of 0.01(energy_increase)
while(found < n):

    psi = np.zeros(total)
    psi1 = np.zeros(total)
    psi2 = np.zeros(total)
    psi1[0] = 0.1
    psi1[-1] = -0.1
    V = potential(x)

    for i in range(1,meet+1):
        # Doing the integration step by step
        psi[i] = psi[i-1] + dx * psi1[i-1]
        psi1[i] = psi1[i-1] + dx * psi2[i-1]
        psi2[i] = -2 * psi[i] * (energy - V[i])
    
    data = psi[meet]
    data1 = psi1[meet]

    for i in range(1,total-meet):
        # Doing the integration step by step
        psi[-i-1] = psi[-i] - dx * psi1[-i]
        psi1[-i-1] = psi1[-i] - dx * psi2[-i]
        psi2[-i-1] = -2 * psi[-i-1] * (energy - V[-i-1])

    k = abs(data1/data - psi1[meet]/psi[meet])

    # A local minima of k will give the best match where the slopes from both sides are equal
    if k_p < k_pp and k_p < k :

        found += 1
        solution(psi_old, psi1_old, psi2_old, databak)
   
    psi_old = psi
    psi1_old = psi1
    psi2_old = psi2
    k_pp = k_p
    k_p = k
    data1bak = data1
    databak = data
    energy += energy_increase

# End