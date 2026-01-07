# This code plots the dataset of Fig. 5b

import numpy as np
import matplotlib.pyplot as plt

fontsize = 20.0
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
    'axes.linewidth': 0.5})

def load_nu(A, omega, gamma):
    """
    load nus for filament
    """
    filename = "./data_fig5b/"+"alpha_Drot_A_{:.2f}_omega_{:.2f}_gamma_{:.2f}.txt".format(A, omega, gamma)
    data = np.loadtxt(filename, skiprows=1)
    Drots = data[:,0]
    alphas = data[:,1]
    sds = data[:,2]
    
    return Drots, alphas, sds
    
saveplot = True

tfinal = 10000
dt = 0.1
t = np.arange(0, tfinal, dt)

A = 0.12
omegas = [np.pi, 2*np.pi, 2*np.pi]
fs = [0.5, 1.0, 1.0]
gammas = [0.5, 0.2, 0.5]

markersize = 7.8
fig, ax = plt.subplots(figsize=(4, 3.85))

# f = 0.5, gamma = 0.5
Drots, alphas, sds = load_nu(A, omegas[0], gammas[0])
ax.errorbar(Drots, alphas, yerr=sds, marker="d", markerfacecolor="gray", 
    markersize=markersize, markeredgecolor="k", linestyle='none', 
    color="gray", capsize=2.0, mew=0.7, elinewidth=1.2, 
    label=r"$f={:.1f},\ \gamma={:.1f}$".format(fs[0], gammas[0]))

# f = 1.0, gamma = 0.2
Drots, alphas, sds = load_nu(A, omegas[1], gammas[1])
ax.errorbar(Drots, alphas, yerr=sds, marker="o", markerfacecolor="red", 
    markersize=markersize, markeredgecolor="dimgray", linestyle='none', 
    color="red", capsize=2.0, mew=0.7, elinewidth=1.2, 
    label=r"$f={:.1f},\ \gamma={:.1f}$".format(fs[1], gammas[1]))

# f = 1.0, gamma = 0.5
Drots, alphas, sds = load_nu(A, omegas[2], gammas[2])
ax.errorbar(Drots, alphas, yerr=sds, marker="^", markerfacecolor="orange", 
    markersize=markersize, markeredgecolor="dimgray", linestyle='none', 
    color="orange", capsize=2.0, mew=0.7, elinewidth=1.2, 
    label=r"$f={:.1f},\ \gamma={:.1f}$".format(fs[2], gammas[2]))

ax.set_xlim([-0.005, 0.105])
ax.set_ylim([0., 1.0])

ax.set_xticks([0, 0.05, 0.1])
ax.set_xticklabels([r'$0$', r'$0.05$', r'$0.10$'], fontsize=fontsize, fontname=fontname)

ax.set_yticks([0, 0.5, 1.0])
ax.set_yticklabels([r'$0$',r'$0.5$',r'$1.0$'], fontsize=fontsize, fontname=fontname)

ax.set_xlabel(r'$D_r\ (\mathrm{rad}^2/\tau_0)$',fontsize=fontsize, labelpad=0)
ax.set_ylabel(r'$\alpha$',fontsize=fontsize)

ax.legend(edgecolor="gray", fontsize=14, handletextpad=0.2, borderpad=0.3, 
          handlelength=1.0, labelspacing=0.25)

fig.savefig("./fig5b.png", bbox_inches='tight', dpi=300)


