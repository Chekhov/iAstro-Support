from math import *
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from pprint import *
from scipy import stats
import click
import statistics
from mpl_toolkits.mplot3d import Axes3D 

# TODO cumulative function input (x,y) -> (x, cum)

def cumulative(y, n_bins = 10):   
    return stats.cumfreq(y, numbins = n_bins).cumcount

# TODO 