from HJAlg import hooke
import numpy as np
import matplotlib.pyplot as plt
import math
import adjustText as at


def cosine(x):
    return math.cos(math.radians(x))


def functionValue(x, n):
    # value = 100.0 * (x[1] - x[0] * x[0]) ** 2 \                       # Rosenbrock
    #        + (1.0 - x[0]) ** 2

    # value = (x[0]**2 - 4*x[1] + 5) + (x[1]**2 - 6*x[1] + 11)           # has min
    value = x[0] ** 2 + x[1] ** 2 + (x[0] * x[1]) - x[0] + 4  # has min
    # value = 2 * x[0]**2 + 2 * x[0] * x[1] + 2 * x[1]**2 - 6 * x[0]     # has min
    return value


# OPTIONS
nvars = 2
startpt = [2, 5]
itermax = 5000
steplength = 0.5  # should be set to a value between 0.0 and 1.0.
eps = 1.0E-07     # the criterion for halting the search for a minimum.

showsteps = False
showStartAndEnd = True
showLines = True
showNumbers = False
OptimizeGraph = False

plt.title("Hook - Jeeves Method")
plt.xlabel("X")
plt.ylabel("Y")

# hooke(nvars, startpt, rho, eps, itermax, f):
it, endpt, points = hooke(2, startpt, steplength, eps, 1000, functionValue)

xs = []
ys = []
for i in range(len(points)):
    xs.append(points[i][0])
    ys.append(points[i][1])
    #annots = plt.annotate(i+1,[xs[i],ys[i]])

plt.scatter(xs, ys, marker='x', c='red')

# starting point
plt.scatter(xs[0], ys[0], c='red', s=15, marker='x')

# end point - minimum
plt.scatter(endpt[0], endpt[1], c='red', s=15)

# Graph plot options
if showNumbers:
    texts = [plt.text(xs[i], ys[i], str(i + 1), ha='center', va='center') for i in range(len(xs))]
    at.adjust_text(texts, xs, ys, arrowprops=dict(arrowstyle='->', color='black'))

if showLines:
    plt.plot(xs, ys)

if showsteps:
    texts = [plt.text(xs[i], ys[i], 'Step ' + str(i + 1), ha='center', va='center') for i in range(len(xs))]
    at.adjust_text(texts, xs, ys, arrowprops=dict(arrowstyle='->', color='black'))

if showStartAndEnd:
    firstPointText = [plt.text(xs[0], ys[0], '  Starting point (' + str(xs[0]) + ',' + str(ys[0]) + ')')]
    endPointText = [plt.text(endpt[0], endpt[1],
                             '   Minimum (' + str(np.round(endpt[0], 2)) + ',' + str(np.round(endpt[1], 2)) + ')')]
    # adjust texts so they dont overlap
    at.adjust_text(firstPointText, xs, ys, arrowprops=dict(arrowstyle='-', color='black'))
    at.adjust_text(endPointText, endpt, endpt, arrowprops=dict(arrowstyle='-', color='black'))

if OptimizeGraph:
    xmin = min(x for x in xs)
    xmax = max(x for x in xs)
    ymin = min(y for y in ys)
    ymax = max(y for y in ys)
    plt.axis([xmin, xmax, ymin, ymax])

plt.savefig('plot.png', dpi=200)
plt.show()
print('')
print('Number of iterations taken = %d' % (it))
print('--------------------------------------------')
print('Last point - minimum equals:\n')
print(np.round(endpt, 2))
