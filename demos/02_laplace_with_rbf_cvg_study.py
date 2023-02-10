# -*- coding: utf-8 -*-
"""RBF Convergence Analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rJlCDzzyW0r44hfN2XeQTEiZlwjMgyhT
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

###
df = pd.read_csv("temp/hparams_table.csv").iloc[2:, :]
df


###
df["h_avg"] = 1/ np.sqrt(df["nb_nodes"])
df

###
x = df["h_avg"]
y = np.sqrt(df["metrics/mse_error"])

from scipy.stats import linregress
res = linregress(np.log(x), np.log(y))

###
fig, ax= plt.subplots(1,1, figsize=(8,5))
ax.loglog(x,y, "x-", label="slope = "+(str(res.slope)[:5]))
ax.set_xlabel("h")    ## Should be h_max here
ax.set_ylabel("RMSE") ## Should be SUM of local error, not MEAN. USE INTERPOLATION !
ax.set_title("Convergence analysis - Laplace problem")
ax.legend();

