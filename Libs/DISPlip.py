from math import *
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from pprint import *
from scipy import stats
import click
import statistics
from mpl_toolkits.mplot3d import Axes3D 

# TODO Display normal function

# TODO ScatterPlot

def twoDimensionalHistPlot(generator, L = 1000):
    x = [generator.next() for k in range(0,L+1)]
    y = [generator.next() for k in range(0,L+1)]
    # definitions for the axes
    left, width = 0.1, 0.65
    bottom, height = 0.1, 0.65
    spacing = 0.005


    rect_scatter = [left, bottom, width, height]
    rect_histx = [left, bottom + height + spacing, width, 0.2]
    rect_histy = [left + width + spacing, bottom, 0.2, height]

    # start with a square Figure
    fig = plt.figure(figsize=(8, 8))

    ax = fig.add_axes(rect_scatter)
    ax_histx = fig.add_axes(rect_histx, sharex=ax)
    ax_histy = fig.add_axes(rect_histy, sharey=ax)

    # use the previously defined function
    scatter_hist(x, y, ax, ax_histx, ax_histy)
    plt.title(r'Spectral Test 2D')

    plt.show()

def scatter_hist(x, y, ax, ax_histx, ax_histy):
    # no labels
    ax_histx.tick_params(axis="x", labelbottom=False)
    ax_histy.tick_params(axis="y", labelleft=False)

    # the scatter plot:
    ax.scatter(x, y, alpha = 0.2, color='k', marker=",")

    # now determine nice limits by hand:
    binwidth = 0.25
    xymax = max(np.max(np.abs(x)), np.max(np.abs(y)))
    lim = (int(xymax/binwidth) + 1) * binwidth

    bins = np.arange(0, lim + binwidth, binwidth)
    ax_histx.hist(x, bins=bins)
    ax_histy.hist(y, bins=bins, orientation='horizontal')

def simpleplot(y):
    plt.plot(y)
    plt.show()