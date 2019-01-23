from tom178 import hooke
import numpy as np
import matplotlib.pyplot as plt
import math
import adjustText as at
#   Input, integer NVARS, the number of spatial dimensions.
#
#    Input, real STARTPT(NVARS), the user-supplied
#    initial estimate for the minimizer.
#
#    Input, real RHO, a user-supplied convergence parameter
#    which should be set to a value between 0.0 and 1.0.

#    Input, real EPS, the criterion for halting
#    the search for a minimum.

#    Input, integer ITERMAX, a limit on the number of iterations.
#
#    Input, function handle F, the name of the function routine,
#    which should have the form:
#      function value = f ( x, n )

#    Output, integer ITERS, the number of iterations taken.
#
#    Output, real ENDPT(NVARS), the estimate for the
#    minimizer, as calculated by the program.
#def hooke(nvars, startpt, rho, eps, itermax, f):


def cosine(x):
    return math.cos(math.radians(x))

def functionValue(x, n):
    # *****************************************************************************
    #  Parameters:
    #
    #    Input, real X(N), the argument of the function.
    #
    #    Input, integer N, the spatial dimension.
    #
    #    Output, real VALUE, the value of the function.
    #
    # value = 100.0 * (x[1] - x[0] * x[0]) ** 2 \
    #        + (1.0 - x[0]) ** 2
    #value = (x[0]**2 - 4*x[1] + 5) + (x[1]**2 - 6*x[1] + 11)
    value = x[0]**2 + x[1]**2 + (x[0] * x[1]) - x[0] + 4
    #value = x[0]**2 + math.cos(cosine(x[1]**2)) + (x[0] * x[1]) - x[1]
    #value = 2 * x[0]**2 + 2 * x[0] * x[1] + 2 * x[1]**2 - 6 * x[0]
    return value

step = 1   # krok
nvars = 2
startpt = [2, 3]
itermax = 5000
rho = 0.5               # a user-supplied convergence parameter which should be set to a value between 0.0 and 1.0.
eps = 1.0E-06           # the criterion for halting the search for a minimum.
x0 = startpt.copy()
d1 = np.array([1, 0])
d2 = np.array([0, 1])
a = x0

showsteps = False
showStartAndEnd = False
optimizeGraph = False


#def hooke(nvars, startpt, rho, eps, itermax, f):
it, endpt, points = hooke(2, startpt, rho, eps, 1000, functionValue)



xs = []
ys = []
print(points)
for i in range(len(points)):
    xs.append(points[i][0])
    ys.append(points[i][1])
    #annots = plt.annotate(i+1,[xs[i],ys[i]])

print(len(xs))
plt.scatter(xs, ys, marker = 'x')

# starting point - yellow
plt.scatter(xs[0], ys[0], c='yellow', s=15, marker = 'x')

# end point red
plt.scatter(endpt[0],endpt[1], c='red', s=15)






plt.title("Hook - Jeeves Method")
plt.xlabel("X")
plt.ylabel("Y")

showsteps = True
#showStartAndEnd = True

if showsteps:
    texts = [plt.text(xs[i], ys[i], 'Step '+ str(i+1) , ha='center', va='center') for i in range(len(xs))]
    at.adjust_text(texts, xs, ys, arrowprops=dict(arrowstyle='->', color='black'))


if showStartAndEnd:
    firstPointText = [plt.text(xs[0], ys[0], 'Starting point (' + str(xs[0]) + ',' + str(ys[0]) + ')')]
    endPointText = [plt.text(endpt[0], endpt[1],'Ending point (' + str(np.round(endpt[0])) + ',' + str(np.round(endpt[1])) + ')')]
    #adjust texts so they dont overlap
    at.adjust_text(firstPointText, xs, ys, arrowprops=dict(arrowstyle='-', color='black'))
    at.adjust_text(endPointText, endpt, endpt, arrowprops=dict(arrowstyle='-', color='black'))

def OptimizeGraph():
    xmin = min(x for x in xs)
    xmax = max(x for x in xs)
    ymin = min(y for y in ys)
    ymax = max(y for y in ys)
    plt.axis([xmin, xmax, ymin, ymax])

plt.show()
print('')
print('Number of iterations taken = %d' % (it))
print('--------------------------------------------')
print('Last point - minimum equals:\n')
print(endpt)