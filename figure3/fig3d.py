# Plot script for figure 3d 

import matplotlib.pyplot as plt
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from paperfig import *


def fig3d_center():
    setup_style(fontsize=22, font="Helvetica", usetex="auto",
                axes_lw=1.0, lines_lw=0.1, tick_size=5.0)

    figsize = (4.0, 3.5)
    fontsize = 22
    ms = 8
    mew = 1
    lw = 1.5

    A = 0.12
    T = 10000
    gamma_list = [0.20, 0.50]
    ls_list = ["-", "--"]
    color_list = ["k", "r"]

    fig, ax = plt.subplots(figsize=figsize)

    data_dir = ROOT / "figure3" / "data_fig3d"

    for i, gamma in enumerate(gamma_list):
        fn = f"center_A_{A:.2f}_gamma_{gamma:.2f}_T_{T:.0f}.txt"
        dat = np.loadtxt(data_dir / fn, delimiter=",", skiprows=1)

        ax.plot(
            dat[:, 0],
            dat[:, 1],
            color=color_list[i],
            marker="o",
            mfc="none",
            ms=ms,
            mew=mew,
            ls=ls_list[i],
            lw=lw,
        )

    # annotations
    ax.annotate(
        r"$\gamma=0.2$",
        xy=(0.3, 0.465),
        xytext=(0.2, 0.515),
        fontsize=fontsize - 2,
        color=color_list[0],
        arrowprops=dict(arrowstyle="<-", color=color_list[0], lw=lw),
    )
    ax.annotate(
        r"$\gamma=0.5$",
        xy=(0.74, 0.465),
        xytext=(0.65, 0.515),
        fontsize=fontsize - 2,
        color=color_list[1],
        arrowprops=dict(arrowstyle="<-", color=color_list[1], lw=lw),
    )

    ax.set_xlabel(r"$f$", labelpad=-2)
    ax.set_ylabel(r"$\langle R \rangle$", labelpad=4, rotation=0, va="center")

    ax.set_yticks([0.3, 0.5])
    ax.set_xticks([0, 0.25, 0.5, 0.75, 1.0])
    ax.set_xticklabels([r"$0$", "", r"$0.5$", "", r"$1.0$"])
    ax.set_xlim(0, 1.06)

    fig.subplots_adjust(left=0.18, bottom=0.17)

    if save_bool:
        save_path = ROOT / "figure3" / "fig3d.png"
        plt.savefig(save_path, dpi=300)
    else:
        plt.show()


if __name__ == "__main__":
    save_bool = True
    fig3d_center()