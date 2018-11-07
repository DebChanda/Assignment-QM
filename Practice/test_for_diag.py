import matplotlib.pyplot as plt
import numpy as np

# Declaring variables
total = 1000
x = np.linspace(0,1,total)
dx = x[1] - x[0]
row_number = 3

phi_array = np.zeros((row_number,total))
phi2_array = np.zeros((row_number,total))

for i in range(row_number):
    phi_array[i] = (2**0.5) * np.sin((i + 1) * np.pi * x)
    phi2_array[i] = phi_array[i] * ((i + 1) * np.pi) **2 



# Check
plt.style.use("ggplot")
plt.plot(x,phi_array[0])
plt.plot(x,phi_array[1])
plt.plot(x,phi_array[2])
# plt.show()

# Genetaing the potential
def potential(x):

    V = np.zeros(total)
    return V

# Genrating the matrix
mat = np.zeros((row_number, row_number))
V = potential(x)

for i in range(row_number):
    for j in range(row_number):
        mat[i][j] = dx * sum(phi_array[i] * phi2_array[j] / 2 + V * phi_array[i] * phi_array[j])

k = np.linalg.eigvals(mat)  
print(mat)
print(k)
print(k.min())
