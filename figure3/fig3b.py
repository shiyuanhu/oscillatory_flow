# Plot script for figure 3b (alpha-gamma).

import matplotlib.pyplot as plt
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from paperfig import *


def fig3b_nu_gamma():
    setup_style(fontsize=22, font="Helvetica", usetex="auto",
                axes_lw=1.0, lines_lw=0.1, tick_size=5.0)

    # ----------------------------
    # settings 
    # ----------------------------
    figsize = (5.0, 4.0)
    ms = 8
    mew = 1
    lw = 1.5
    per_data = 1

    fig, ax = plt.subplots(figsize=figsize, dpi=300)

    data_path = ROOT / "figure3" / "data_fig3b"
    data = np.loadtxt(data_path / "alpha_gamma_A_0.12_omega_3.14.txt", delimiter=",", skiprows=1)

    ax.errorbar(
        data[::per_data, 0],
        data[::per_data, 1],
        data[::per_data, 2],
        ls="none",
        mew=mew,
        mfc="none",
        color="k",
        marker="o",
        markersize=ms,
        linewidth=lw,
        capsize=3,
        alpha=0.8,
    )

    ax.set_xlabel(r"$\gamma$", labelpad=-2)
    ax.set_ylabel(r"$\alpha$", labelpad=15, rotation=0, va="center")

    ax.set_xticks([0, 0.2, 0.4, 0.6, 0.8])
    ax.set_yticks([0, 1, 2])
    ax.set_xticklabels([r"$0$", "", r"$0.4$", "", r"$0.8$"])
    ax.set_xlim([-0.02, 0.85])
    ax.set_ylim([0, 2.1])

    fig.subplots_adjust(left=0.18, bottom=0.17)

    if save_bool:
        save_path = ROOT / "figure3" / "fig3b.png"
        plt.savefig(save_path, dpi=300)
    else:
        plt.show()


if __name__ == "__main__":
    save_bool = True
    fig3b_nu_gamma()