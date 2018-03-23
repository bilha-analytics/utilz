## 1. Load libraries and set env 

## data structures and manipulation 
import pandas as pd
import numpy as np 

## visualization 
import seaborn as sns
import matplotlib.pyplot as plt 

## particular datatypes manipulation 
from dateutil.parser import parse

## statistical analysis - Ho-testing and glm Regression 
import statsmodels.api as sm
import statsmodels.formula.api as smf
## patsy is a Python library for describing statistical models and building Design Matrices using R-like formulas.
import patsy 

import scipy.stats as sci 
import math 


## Shared Env
%matplotlib inline 
plt.style.use('seaborn-white')
sns.set(color_codes=True)


## Getting R in the mix =D  << TODO: put R libs in a seperate Rscript file and load it from here<<< Excited!!!!!
# %load_ext rpy2.ipython 
# %R require(ggplot2); require(tidyr); require(dplyr) 