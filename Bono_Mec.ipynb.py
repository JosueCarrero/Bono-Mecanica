import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 100, 10000)
w_1 = 6.5
r_i = 0.001

def phi(t, w):
    return w * t

def r(phif, r_1):
    return (r_i / 2) * np.exp(phif) + (r_i / 2) * np.exp(-phif)

def plot_recorrido(w, r_i):
    t = np.linspace(0, 100, 10000)
    phi2 = phi(t, w)
    radial = r(phi2, r_i)
    x = radial * np.cos(phi2)
    y = radial * np.sin(phi2)

    plt.plot(x, y)
    plt.grid()
    plt.axhline(0, color='red')
    plt.axvline(0, color='red')
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)
    plt.show()

plot_recorrido(w_1, r_i)