import math

def cosine(x):
    return math.cos(math.radians(x))


def getValue(x, n):
    # value = 100.0 * (x[1] - x[0] * x[0]) ** 2 \                       # Rosenbrock
    #        + (1.0 - x[0]) ** 2

    #value = (x[0]**2 - 4*x[1] + 5) + (x[1]**2 - 6*x[1] + 11)           # has min
    value = x[0] ** 2 + x[1] ** 2 + (x[0] * x[1]) - x[0] + 4  # has min
    #value = 2 * x[0]**2 + 2 * x[0] * x[1] + 2 * x[1]**2 - 6 * x[0]     # has min
    return value
