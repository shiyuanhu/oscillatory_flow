# Plot script for figure 2b.

import matplotlib.pyplot as plt
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from paperfig import *


def fig2b_trap_L_simu():
    """
    Fig 2b: Simulation trapping time fraction vs gamma (final).
    Uses errorbar (no interpolation), matching legacy style.
    """
    setup_style(fontsize=22, font="Helvetica", usetex="auto",
                axes_lw=1.0, lines_lw=0.1, tick_size=5.0)

    # ----------------------------
    # Plot settings (all here)
    # ----------------------------
    figsize = (4.8, 4)
    ms = 8
    lw = 2
    legend_title = 22 - 5.5
    legend_fontsize = 22 - 6.5
    frameon = True
    ylabelpad = 5
    xlabelpad = 0
    left = 0.18
    bottom = 0.17

    # ----------------------------
    # Data files (exported)
    # ----------------------------
    data_dir = ROOT / "figure2" / "data_fig2b"

    files = [
        ("trap_L_simu_A_0.00_omega_3.14.txt", "Black",  "o", r"$0,  0$"),
        ("trap_L_simu_A_0.12_omega_3.14.txt", "orange", "^", r"$0.5,  0.12$"),
        ("trap_L_simu_A_0.15_omega_3.14.txt", "red",    "o", r"$0.5,  0.15$"),
    ]

    fig, ax = plt.subplots(figsize=figsize, dpi=300)

    per_data = 1
    for fn, color, marker, legend in files:
        dat = np.loadtxt(data_dir / fn, delimiter=",", skiprows=1)
        gamma = dat[::per_data, 0]
        mean  = dat[::per_data, 1]
        std   = dat[::per_data, 2]

        ax.errorbar(
            gamma, mean, std,
            capsize=3,
            label=legend,
            ls="none",
            color=color,
            lw=lw - 0.6,
            marker=marker,
            mfc="none",
            markersize=ms,
        )

    ax.legend(
        loc="lower left",
        ncol=1,
        title=r"$f, A_\mathrm{f}$",
        title_fontsize=legend_title,
        fontsize=legend_fontsize - 1,
        frameon=frameon,
        edgecolor="k",
        handletextpad=1,
        handlelength=1,
        columnspacing=0.5,
    )

    ax.set_xlim([0.1, 0.94])
    ax.set_ylim([0.16, 1.03])
    ax.set_xticks([0.1, 0.5, 0.9])
    ax.set_yticks([0.2, 0.6, 1])

    ax.set_ylabel(r"$\tilde{T}_{\mathrm {trap}}$", labelpad=ylabelpad)
    ax.set_xlabel(r"$\gamma$", labelpad=xlabelpad)
    ax.minorticks_off()

    fig.subplots_adjust(left=left, bottom=bottom)

    if save_bool:
        save_path = ROOT / "figure2" / "fig2b.png"
        plt.savefig(save_path, dpi=300)
    else:
        plt.show()


if __name__ == "__main__":
    save_bool = True
    fig2b_trap_L_simu()