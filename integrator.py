import os
import time

start = time.time()
os.system("clear")


def func(energy, x, power):
    dummy = 4 * ((2 * (energy - x**power))**0.5)
    return dummy


def integrate(energy, power):
    ulim = energy ** (1 / power)
    llim = 0
    div = 15000
    min_div = (ulim - llim) / div
    x_value = []
    for i in range(int(div) + 1):
        x_value.append(llim + i * min_div)

    value = 0
    for i in range(div):
        xs = x_value[i]
        dummy = func(energy, xs, power)
        value += dummy

    ans = value * min_div
    # print("For energy ", energy, "value is", ans)
    return ans


def check_integer(value, integer, min_div):
    if (value >= integer - min_div):
        if (value <= integer + min_div):
            return "ok"
        else:
            return "large"
    else:
        return "less"


power = int(input("Enter the power of 'x' in V(x) : "))
number = int(input("Enter the number of states : "))
# accuracy = int(input("Enter accuracy, digit after decimal upto which you want the answer to be accurate:"))
alpha = 2 * power
beta = 2
gamma = -power

accuracy = 4
start_energy = 0.0
min_div = 10**(-accuracy)
mod1 = 1
mod2 = 0.1

print("Energy will be in units of (h^({})k^({})m^({}))^1/{}".format(alpha, beta, gamma, (2 + power)))
for i in range(1, number + 1):
    mod = mod1
    energy_data = [start_energy, start_energy]
    not_found = True
    less_value = 0.0
    large_value = 0.0
    while(not_found):
        pxdx = integrate(energy_data[0], power)
        confirm = check_integer(pxdx, i, min_div)
        if confirm == "less":
            # print("less")
            less_value = energy_data[0]
            energy_data[0] = less_value + mod
        elif confirm == "large":
            # print("large")
            large_value = energy_data[0]
            energy_data[0] = less_value + mod * mod2
            energy_data[1] = large_value
            mod = mod * mod2
        else:
            not_found = False
            stored_energy = energy_data[0]
            check = 0
            while(confirm == "ok"):
                pxdx = integrate(stored_energy + check * mod, power)
                confirm = check_integer(pxdx, i, min_div)
                check += 1

            final_answer = stored_energy + mod * (check - 2)
            print("The modf-energy for state {} is : {:.{}f}.\n".format(i, final_answer, accuracy))

print("Time taken : {}".format(time.time() - start))
