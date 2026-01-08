# Plot script for figure 2a.

import matplotlib.pyplot as plt
import sys
from pathlib import Path
from scipy.interpolate import CubicSpline  

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from paperfig import *


def fig2a_trap_L_exp():
    setup_style(fontsize=22, font="Helvetica", usetex="auto",
                axes_lw=1.0, lines_lw=0.1, tick_size=5.0)

    # ----------------------------
    # Plot settings
    # ----------------------------
    figsize = (4.8, 4)
    ms = 8
    mew = 0.8
    lw = 2
    legend_title = 22 - 5.5
    legend_fontsize = 22 - 6.5
    alpha = 0.15
    markers_local = ["o", "o", "o"]
    frameon = True
    edgecolor = "k"
    xlabelpad = 0
    ylabelpad = 5
    left = 0.18
    bottom = 0.17
    nsmooth = 50

    data_dir = ROOT / "figure2" / "data_fig2a"
    files = [
        ("trap_L_exp_A_0.00_f_0.00.txt", "Black", r"$0,\ 0$"),
        ("trap_L_exp_A_0.15_f_0.50.txt", "Red",   r"$0.5, \ 0.15$"),
    ]

    fig, ax = plt.subplots(figsize=figsize, dpi=300)

    for i, (fn, color, legend) in enumerate(files):
        dat = np.loadtxt(data_dir / fn, delimiter=",", skiprows=1)
        gamma = dat[:, 0]
        mean = dat[:, 1]
        std = dat[:, 2]

        ax.plot(
            gamma, mean,
            label=legend,
            ls="none",
            marker=markers_local[i],
            lw=lw,
            markersize=ms,
            mfc=color,
            mew=mew,
            mec="dimgrey",
        )

        # ---- smooth error band  ----
        lower_env = mean - std
        upper_env = mean + std

        # spline (natural bc)
        lowerband = CubicSpline(gamma, lower_env, bc_type="natural")
        upperband = CubicSpline(gamma, upper_env, bc_type="natural")

        xsmooth = np.linspace(gamma.min(), gamma.max(), nsmooth)
        ylower = lowerband(xsmooth)
        yupper = upperband(xsmooth)

        ax.fill_between(xsmooth, yupper, ylower, color=color, alpha=alpha, lw=0)

    ax.set_xlim([0.1, 0.9])
    ax.set_ylim([0.45, 1.04])
    ax.set_xticks([0.1, 0.5, 0.9])

    ax.legend(
        loc="lower left",
        title=r"$f, A_{\mathrm{f}}$",
        ncols=1,
        columnspacing=0.3,
        labelspacing=0.3,
        title_fontsize=legend_title,
        fontsize=legend_fontsize,
        frameon=frameon,
        edgecolor=edgecolor,
        handletextpad=0.5,
        handlelength=1,
    )

    ax.set_ylabel(r"$\tilde{T}_{\mathrm {trap}}$", labelpad=ylabelpad)
    ax.set_xlabel(r"$\gamma$", labelpad=xlabelpad)
    ax.minorticks_off()

    fig.subplots_adjust(left=left, bottom=bottom)

    if save_bool:
        save_path = ROOT / "figure2" / "fig2a.png"
        plt.savefig(save_path, dpi=300)
    else:
        plt.show()


if __name__ == "__main__":
    save_bool = False
    fig2a_trap_L_exp()