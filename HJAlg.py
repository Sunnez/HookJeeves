import matplotlib.pyplot as plt
import os

fig = plt.figure()



def best_nearby(delta, point, prevbest, nvars, f, funevals):

    z = point.copy()

    minf = prevbest

    for i in range(0, nvars):

        z[i] = point[i] + delta[i]

        ftmp = f(z, nvars)
        funevals = funevals + 1

        if (ftmp < minf):

            minf = ftmp

        else:

            delta[i] = - delta[i]
            z[i] = point[i] + delta[i]
            ftmp = f(z, nvars)
            funevals = funevals + 1

            if (ftmp < minf):
                minf = ftmp
            else:
                z[i] = point[i]

    point = z.copy()

    newbest = minf

    return newbest, point, funevals


def hooke(nvars, startpt, rho, eps, itermax, f):

    import numpy as np

    verbose = True
    points = []
    newx = startpt.copy()
    xbefore = startpt.copy()

    delta = np.zeros(nvars)

    for i in range(0, nvars):
        if startpt[i] == 0.0:
            delta[i] = rho
        else:
            delta[i] = rho * abs(startpt[i])

    funevals = 0
    steplength = rho
    iters = 0
    fbefore = f(newx, nvars)
    funevals = funevals + 1
    newf = fbefore

    while iters < itermax and eps < steplength:

        iters = iters + 1

        if (verbose):

            print('')
            print('  FUNEVALS = %d, F(X) = %g' % (funevals, fbefore))
            pair = []
            for i in range(0, nvars):
                print('  %8d  %g' % (i, xbefore[i]))
                pair.append(xbefore[i])
                if len(pair) == 2:
                    points.append(pair)

        #
        #  Find best new point, one coordinate at a time.
        #
        for i in range(0, nvars):
            newx[i] = xbefore[i]
        newf, newx, funevals = best_nearby(delta, newx, fbefore, nvars, f, funevals)
        #
        #  If we made some improvements, pursue that direction.
        #
        keep = True
        while (newf < fbefore and keep):

            for i in range(0, nvars):
                #
                #  Arrange the sign of DELTA.
                #
                if (newx[i] <= xbefore[i]):
                    delta[i] = - abs(delta[i])
                else:
                    delta[i] = abs(delta[i])
                #
                #  Now, move further in this direction.
                #
                tmp = xbefore[i]
                xbefore[i] = newx[i]
                newx[i] = newx[i] + newx[i] - tmp

            fbefore = newf
            newf, newx, funevals = best_nearby(delta, newx, fbefore, nvars, f, funevals)
            #
            #  If the further (optimistic) move was bad...
            #

            if (fbefore <= newf):
                break
            #
            #  Make sure that the differences between the new and the old points
            #  are due to actual displacements; beware of roundoff errors that
            #  might cause NEWF < FBEFORE.
            #
            keep = False

            for i in range(0, nvars):
                if (0.5 * abs(delta[i]) < abs(newx[i] - xbefore[i])):
                    keep = True
                    break

        if (eps <= steplength and fbefore <= newf):
            steplength = steplength * rho
            for i in range(0, nvars):
                delta[i] = delta[i] * rho

    endpt = xbefore.copy()

    return iters, endpt, points