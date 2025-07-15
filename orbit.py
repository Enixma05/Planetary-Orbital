import matplotlib.pyplot as plt
import numpy as np

# Membuat 100 titik dari 0 hingga 2π (1 putaran penuh)
theta = np.linspace(0, 2*np.pi, 100)

# (orbit lingkaran sempurna)
# r = 1  # radius orbit

# (orbit elips)
a_b = 1.0
b_b = 0.8
e_b = 0.6  # bumi
a_m = 2.0
b_m = 1.8
e_m = 1.5  # mars

# Menghitung koordinat x dan y
x_b = b_b * np.cos(theta) - e_b * np.sin(theta)
y_b = b_b * np.sin(theta)

x_m = b_m * np.cos(theta) - e_m * np.sin(theta)
y_m = b_m * np.sin(theta)

for i in range(len(theta)):
    plt.cla()
    plt.plot(x_b, y_b, 'k', label="Orbit Bumi")  # orbit Bumi
    plt.plot(x_b[i], y_b[i], 'bo', label="Bumi")  # posisi Bumi
    plt.plot(x_m, y_m, 'k', label="Orbit Mars")  # orbit Mars
    plt.plot(x_m[i], y_m[i], 'ro', label="Mars")  # posisi Mars
    plt.plot(0, 0, 'yo', label="Matahari")  # Posisi Matahari
    plt.xlim(-3, 3)
    plt.ylim(-3, 3)
    plt.legend()
    plt.title("Orbit Planet Sederhana (Elips)")
    plt.pause(0.05)
