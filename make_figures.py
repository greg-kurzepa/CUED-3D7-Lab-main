import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

results_folder = "results"

filenames = [
    "asymmetric_results_logarithmic.csv",
    "asymmetric_results_quadratic.csv",
    "asymmetric_results_quartic.csv",
]
labels = [
    "logarithmic",
    "quadratic",
    "quartic",
]

dfs = []
for fn in filenames:
    dfs.append(pd.read_csv(os.path.join(results_folder, fn)))

fig, ax = plt.subplots(1,2, sharey=True)

for idx, df in enumerate(dfs):
    print(df)
    ax[0].plot(df["Element Count"], df["Max Von Mises Stress (Mpa)"], label=labels[idx])
    ax[1].plot(df["Elapsed Time (s)"], df["Max Von Mises Stress (Mpa)"], label=labels[idx])
ax[0].grid()
ax[0].legend()
ax[1].grid()
ax[1].legend()
plt.show()