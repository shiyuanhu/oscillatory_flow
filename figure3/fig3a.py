# Plot script for figure 3a (island contribution panel).

import matplotlib.pyplot as plt
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from paperfig import *


def fig3a_island_contri():
    setup_style(fontsize=22, font="Helvetica", usetex="auto",
                axes_lw=1.0, lines_lw=0.1, tick_size=5.0)

    # ----------------------------
    # Settings 
    # ----------------------------
    ms = 8
    mew = 0.8
    legend_fontsize = 16
    per_data = 2

    A = 0.12
    omega = np.pi
    T = 300
    circle_num = 10

    data_path = ROOT / "figure3" / "data_fig3a"
    fn = f"island_contri_A_{A:.2f}_omega_{omega:.2f}_T_{T:.0f}_circle_{circle_num}.txt"
    dat = np.loadtxt(data_path / fn, delimiter=",", skiprows=1)

    gamma = dat[:, 0]
    total = dat[:, 1]
    chaotic = dat[:, 2]
    elliptic = dat[:, 3]

    fig, ax = plt.subplots(figsize=(5.0, 4.0))

    # total
    ax.plot(
        gamma[::per_data], total[::per_data],
        color="k", label="total",
        marker="o", markersize=ms,
        mec="k", mfc="none", mew=mew,
        ls="none",
    )

    markers_local = ["o", ">", "^"]
    colors_local = ["Lightgrey", "Blue", "Red"]
    labels = ["chaotic", "elliptic"]

    ax.plot(
        gamma[::per_data], chaotic[::per_data],
        label=labels[0],
        color=colors_local[0],
        marker=markers_local[0],
        markersize=ms,
        mew=0.6,
        ls="none",
        mec="dimgrey",
        mfc=colors_local[0],
        alpha=1,
    )

    ax.plot(
        gamma[::per_data], elliptic[::per_data],
        label=labels[1],
        color=colors_local[1],
        marker=markers_local[1],
        markersize=ms,
        mew=0.6,
        ls="none",
        mec="dimgrey",
        mfc=colors_local[1],
        alpha=1,
    )

    ax.set_xlim([-0.02, 0.82])
    ax.set_ylim([-0.04, 1.25])
    ax.set_xticks([0, 0.2, 0.4, 0.6, 0.8])
    ax.set_yticks([0, 0.5, 1])
    ax.set_xticklabels([r"$0$", "", r"$0.4$", "", r"$0.8$"])
    ax.set_yticklabels([r"$0$", "", r"$1$"])

    ax.set_ylabel(r"$\tilde{T}_{\mathrm{trap}}$", labelpad=0)
    ax.set_xlabel(r"$\gamma$", labelpad=0)
    ax.minorticks_off()

    ax.legend(
        ncol=1,
        loc="upper left",
        columnspacing=1,
        fontsize=legend_fontsize - 1,
        handletextpad=0.6,
        edgecolor="k",
        labelspacing=0.4,
        handlelength=0.5,
    )

    fig.subplots_adjust(left=0.18, bottom=0.17)
    if save_bool:
        save_path = ROOT / "figure3" / "fig3a.png"
        plt.savefig(save_path, dpi=300)
    else:
        plt.show()


if __name__ == "__main__":
    save_bool = False
    fig3a_island_contri()