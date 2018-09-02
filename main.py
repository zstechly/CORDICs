import numpy as np


# rotating signal to baseband (vector mode)

# x(n+1) = x(n) - y(n) * d(n) * 2^(-n)
# y(n+1) = y(n) + x(n) * d(n) * 2^(-n)
# z(n+1) = z(n) - d(n) * arctan(2^(-n))
x = np.cos(np.pi/3)
y = np.sin(np.pi/3)
z = 0
d = 0
for i in range(10):
#    print(np.arctan(2**-i))
    if (y < 0):
        d = 1
    else:
        d = -1;
    x_next = x - y * d * 2**-i
    y_next = y + x * d * 2**-i
    z_next = z - d * np.arctan(2**-i)
    x = x_next
    y = y_next
    z = z_next

print("x: " + str(x))
print("y: " + str(y))
print("z: " + str(z))


# rotate signal away from baseband (rotation mode)
x = 1
y = 0
z = np.pi/3
d = 0

for i in range(10):
    #    print(np.arctan(2**-i))
    if (z < 0):
        d = -1
    else:
        d = 1
    x_next = x - y * d * 2**-i
    y_next = y + x * d * 2**-i
    z_next = z - d * np.arctan(2**-i)
    x = x_next
    y = y_next
    z = z_next

print("x: " + str(x))
print("y: " + str(y))
print("z: " + str(z))


# generate sine / cosine using rotation mode
# simply set X = 1, Y = 0.  Calculates both Sine / Cosine
#TODO: Call rotation function once I make it
