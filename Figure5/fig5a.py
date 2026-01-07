# This code plots the dataset of Fig. 5a

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

fontsize = 20
fontname = "Helvetica"
plt.rcParams.update({
    "axes.labelsize": fontsize,
    "xtick.labelsize": fontsize,
    "ytick.labelsize": fontsize,
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.sans-serif": [fontname],
    'xtick.direction': 'in',
    'ytick.direction': 'in',
    'xtick.major.size': 5,
    'ytick.major.size': 5,
    'axes.linewidth': 0.5})

# characteristic size of islands
island_data = np.loadtxt("./data_fig5a/island_size.txt", skiprows=1)
As = island_data[:,0]
Wl = island_data[:,1]
Ws = island_data[:,2]

# peak positions of alpha-gamma relation
data = np.loadtxt("./data_fig5a/gamma_s.txt", skiprows=1)
gamma_s = data[:,1]
sd_s = data[:,-2:].T

data = np.loadtxt("./data_fig5a/gamma_l.txt", skiprows=1)
gamma_l = data[:,1]
sd_l = data[:,-2:].T

####
fig, ax = plt.subplots(figsize=(4, 3.85))

result = linregress(As, Wl)
linear_guess = -2.0*As + 0.74

# plot large island
ax.plot(As, Wl, color='blue', marker='o', linestyle='none', 
        markerfacecolor='none', label=r"$W_l$", markersize=7.5)
ax.errorbar(As, gamma_l, yerr=sd_l, marker='o', linestyle='none', 
            capsize=2.0, markeredgewidth=0.7, color='blue', markerfacecolor='blue',
            markeredgecolor="dimgray", markersize=7.5, label=r"$\gamma_l$")

ax.plot(As, linear_guess, color='blue', linestyle="--")

ax.text(0.19, 0.34, r"$\sim -2 A_{\mathrm{f}}$", fontsize=fontsize-2, 
        rotation=-17)

# plot small island
ax.plot(As, Ws, color='red', marker='o', linestyle='none', 
        markerfacecolor='none', markersize=7.5, label=r"$W_s$")
ax.errorbar(As, gamma_s, yerr=sd_s, marker='o', color='red', markerfacecolor='red', 
            linestyle='none', markeredgecolor="dimgray", capsize=2.0, 
            markersize=7.5, label=r"$\gamma_s$")

ax.set_xlim([0.11, 0.27])
ax.set_xticks([0.15, 0.25])
ax.set_xticklabels([r"$0.15$", r"$0.25$"], fontsize=fontsize)
ax.set_ylim([0, 0.85])
ax.set_yticks([0, 0.4, 0.8])
ax.set_yticklabels([r"$0$", r"$0.4$", r"$0.8$"], fontsize=fontsize)

ax.set_xlabel(r"$A_{\mathrm{f}}/W$")
ax.set_ylabel(r"$\mathrm{length}/W$")

ax.legend(ncols=2, edgecolor="gray", handletextpad=0.2, fontsize=15, borderpad=0.24, 
          handlelength=1.0, labelspacing=0.2, columnspacing=0.6)

fig.savefig("./fig5a.png", dpi=300, bbox_inches="tight")

plt.show()



