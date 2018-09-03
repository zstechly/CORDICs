Working through the paper on CORDIC (COordinate Rotation 
DIgital Computer) located at:

http://www.andraka.com/files/crdcsrvy.pdf

I always forget how these work and have to relearn, so hopefully
this repo will help in that process

It appears the cordic can only sum +/- 90

See Sum[atan(2^-n),0,10] goes to ~1.72 radians
To compensate, rotate to quadrants 1/4, remove 
appropriate amount from angle, and negate 
plus or swap I/Q depending on the operation





CORDIC can operate in vector mode or rotational mode

Vector Mode:

    # x(n+1) = x(n) - y(n) * d(n) * 2^(-n)
    # y(n+1) = y(n) + x(n) * d(n) * 2^(-n)
    # z(n+1) = z(n) - d(n) * arctan(2^(-n))
    

Rotational Mode:

    # x(n+1) = x(n) - y(n) * d(n) * 2^(-n)
    # y(n+1) = y(n) + x(n) * d(n) * 2^(-n)
    # z(n+1) = z(n) - d(n) * arctan(2^(-n))
