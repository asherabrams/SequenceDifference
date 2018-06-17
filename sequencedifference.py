# ASHER ABRAMS - BEGINNING PYTHON PROJECT - 2018-02-07
# C 2018 | 5778 BY ASHER ABRAMS
# This CLI program approximates the derivative from the definition, using the x+h, x-h method.

i = 0
x = 0.0
y = 0.0
ym = 0.0
yp = 0.0
h = 0.01
d = 1.0
iterations = 20

# Declaring x as a float eventually leads to rounding errors, even if you increment by something like 0.1.
# A more streamlined version would cap precision at maybe 3 decimal places with rounding.

import math
def func01(x):
    return x**2
    
# func01 can be any differentiable function supported by Python.
# Current version shows x**2 but I've tested it with math.sin(x).
# I am keeping the import math line as a placeholder and as a learning device,
# because much of the code I'm likely to write will involve math.

while (i <= iterations):
    x = x + 0.1
    y = func01(x)
    ym = func01(x-h)
    yp = func01(x+h)
    d = (yp-ym) / (2*h)
    i = i+1
    print(x)
    print(y)
    print(d)
    print()



