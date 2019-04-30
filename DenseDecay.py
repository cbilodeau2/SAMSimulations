# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 12:55:45 2019

@author: camil
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.cm as cm
import matplotlib.colors as col
from scipy.optimize import curve_fit
import pandas as pd
from math import factorial
import igraph
from igraph import *
import random
import time


## DEFINE DISTANCE DECAY: --------------------------------------------------

def DenseDecay(distance):
    density = 1/(distance**6)
    return density