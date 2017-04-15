#numpy examples
import numpy as np

print(np.__version__)

#some useful examples

#Create and array fro -1 to 1 with intervals of .1
x = np.linspace(-1, 1, 21)
print(x)

#same thing bu in logarithmic space
x = np.logspace(-1, 1, 8, base=10)
print(x)

#Random number generation
tmp = np.random.uniform(size=10)
print(tmp)
ra = np.random.random_integers(0, 10, 10)#10 numbers between 0 and 10
print(ra)

