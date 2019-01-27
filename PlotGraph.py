import numpy as np
import matplotlib.pyplot as plt
import adjustText as at

# OPTIONS
# nvars = 2         # wymiar
# startpt = [6,7]  # punkt startowy
# itermax = 1500    # maks liczba iteracji
# steplength = 0.5  # should be set to a value between 0.0 and 1.0. inaczej rho
# eps = 1.0E-04     # the criterion for halting the search for a minimum.


def PlotGraph(endpt, points, showNumbers, showLines, showSteps, showStartAndEnd):
    fig = plt.figure()
    plt.title("Hook - Jeeves Method")
    plt.xlabel("X")
    plt.ylabel("Y")

    xs = []
    ys = []
    for i in range(len(points)):
        xs.append(points[i][0])
        ys.append(points[i][1])

    # plot points
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

    if showSteps:
        texts = [plt.text(xs[i], ys[i], 'Step ' + str(i + 1), ha='center', va='center') for i in range(len(xs))]
        at.adjust_text(texts, xs, ys, arrowprops=dict(arrowstyle='->', color='black'))

    if showStartAndEnd:
        firstPointText = [plt.text(xs[0], ys[0], '  Starting point (' + str(xs[0]) + ',' + str(ys[0]) + ')')]
        endPointText = [plt.text(endpt[0], endpt[1],
                                 '   Minimum (' + str(np.round(endpt[0], 2)) + ',' + str(np.round(endpt[1], 2)) + ')')]
        # adjust texts so they dont overlap
        at.adjust_text(firstPointText, xs, ys, arrowprops=dict(arrowstyle='-', color='black'))
        at.adjust_text(endPointText, endpt, endpt, arrowprops=dict(arrowstyle='-', color='black'))


    plt.savefig('plot.png', dpi=200)
    plt.show()
    return fig