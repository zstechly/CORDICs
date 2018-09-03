import numpy as np
import matplotlib.pyplot as plt

def adjustQuadrant(z):
    quadrant = 1
    # handle positive rotation
    if (z > 3 * np.pi / 2):
        z = z - 3 * np.pi / 2
        quadrant = 4
    elif (z > np.pi):
        z = z - np.pi
        quadrant = 3
    elif (z > np.pi / 2):
        z = z - np.pi / 2
        quadrant = 2

   # handle negative rotation
    if (z < -3 * np.pi / 2):
        z = z + 3*np.pi/2
        quadrant = 2
    elif (z < -np.pi):
        z = z + np.pi
        quadrant = 3
    elif (z < -np.pi / 2):
        z = z + np.pi / 2
        quadrant = 4

    return z, quadrant

def vectorMode(x, y, iterations=10):
    # rotate a signal to baseband, accumulate angle transversed
    # x(n+1) = x(n) - y(n) * d(n) * 2^(-n)
    # y(n+1) = y(n) + x(n) * d(n) * 2^(-n)
    # z(n+1) = z(n) - d(n) * arctan(2^(-n))

    z = 0
    for i in range(iterations):
        #    print(np.arctan(2**-i))
        if (y < 0):
            d = 1
        else:
            d = -1;
        x_next = x - y * d * 2 ** -i
        y_next = y + x * d * 2 ** -i
        z_next = z - d * np.arctan(2 ** -i)
        x = x_next
        y = y_next
        z = z_next

    return x, y, z


def rotationMode(x, y, z, iterations=10, filename='rotation_test.csv', debug=False):
    # rotates signal away from baseband
    # x(n+1) = x(n) - y(n) * d(n) * 2^(-n)
    # y(n+1) = y(n) + x(n) * d(n) * 2^(-n)
    # z(n+1) = z(n) - d(n) * arctan(2^(-n))

    if (debug == True):
        f0 = open(filename, "w")

    # print("Z initial: " + str(z))
    if (debug == True):
        f0.write("Z initial: " + str(z) + "\n")

    if (debug == True):
        f0.write("current_angle, i, d, x, y, x_next, y_next, z, z_next, z_deg, z_deg_next\n")

    z, quadrant = adjustQuadrant(z)

    for i in range(iterations):
        if (z < 0):
            d = -1
        else:
            d = 1
        x_next = x - y * d * 2 ** -i
        y_next = y + x * d * 2 ** -i
        z_next = z - d * np.arctan(2 ** -i)
        if (debug == True):
            f0.write(str(np.arctan(y / x) * 180 / np.pi) + ",")
            f0.write(str(i) + ",")
            f0.write(str(d) + ",")
            f0.write(str(x) + "," + str(y) + ",")
            f0.write(str(x_next) + "," + str(y_next) + ",")
            f0.write(str(z) + "," + str(z_next) + ",")
            f0.write(str(z * 180 / np.pi) + "," + str(z_next * 180 / np.pi) + "\n")
        x = x_next
        y = y_next
        z = z_next

    if (debug == True):
        f0.close()
    x_out = x
    y_out = y
    if (quadrant == 1):
        x_out = x
        y_out = y
    if (quadrant == 2):
        x_out = -y
        y_out = x
    if (quadrant == 3):
        x_out = -x
        y_out = -y
    if (quadrant == 4):
        x_out = y
        y_out = -x

    return x_out, y_out, z


# rotating signal to baseband (vector mode)

x = np.cos(np.pi / 3)
y = np.sin(np.pi / 3)
z = 0
d = 0

vectorMode(x, y)


# generate sine / cosine using rotation mode
# simply set X = 1, Y = 0.  Calculates both Sine / Cosine
#rotationMode(1, 0, -np.pi/3, filename="./data/rotation_neg45.csv", debug=True)

## generate a cos, sine wave
wave_length = 1024
cos_out = np.zeros(wave_length)
sin_out = np.zeros(wave_length)
freq_vector = np.linspace(-2*np.pi, 2*np.pi, wave_length)
for x in range(cos_out.size):
    cos_out[x], sin_out[x], z = rotationMode(1, 0, freq_vector[x])

plt.plot(cos_out, label='cosine')
plt.plot(sin_out, label='sine')
plt.title('CORDIC Generated Signals')
plt.xlabel('Sample Index')
plt.ylabel('Amplitude')
plt.legend()
plt.grid()
plt.show()
