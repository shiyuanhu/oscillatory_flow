# Plot script for figure 4a.

import matplotlib.pyplot as plt
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from paperfig import *


def plot_fig4a():
    # ----------------------------
    # Settings
    # ----------------------------
    fontsize = 18
    ms = 7
    mew = 0.8
    lw = 1
    legend_fontsize = fontsize - 3

    A = 0.12
    omega = 2 * np.pi
    T = 300
    circle_num = 10
    per_data = 2

    setup_style(
        fontsize=fontsize,
        font="Helvetica",
        usetex="auto",
        axes_lw=1.0,
        lines_lw=0.1,
        tick_size=5.0,
    )

    fig, ax = plt.subplots(figsize=(4.2, 4.0), dpi=300)

 
    data_dir = ROOT / "figure4" / "data_fig4a"
    fn = f"island_contri_ag3_A_{A:.2f}_omega_{omega:.2f}_T_{T:.0f}_circle_{circle_num}_period_6.txt"
    fpath = data_dir / fn
    if not fpath.exists():
        raise FileNotFoundError(f"Missing final data file:\n  {fpath}\n"
                                f"Export it first with np.savetxt() into figure4/data_fig4a/")

    dat = np.loadtxt(fpath, delimiter=",", skiprows=1)

    gamma   = dat[:, 0]
    total   = dat[:, 1]
    chaotic = dat[:, 2]
    period1 = dat[:, 3]
    period3 = dat[:, 4]

    # ----------------------------
    ax.plot(
        gamma[::per_data],
        total[::per_data],
        color="k",
        marker="o",
        markersize=ms,
        mec="k",
        mfc="none",
        mew=mew,
        ls="none",
    )

    markers_local = ["o", ">", "^"]
    colors_local = ["Lightgrey", "Blue", "Red"]
    labels_local = ["chaotic", "period-1", "period-3"]

    ax.plot(
        gamma[::per_data],
        chaotic[::per_data],
        label=labels_local[0],
        color=colors_local[0],
        marker=markers_local[0],
        markersize=ms,
        mew=1,
        ls="none",
        mec="dimgrey",
        mfc=colors_local[0],
        alpha=1,
    )
    ax.plot(
        gamma[::per_data],
        period1[::per_data],
        label=labels_local[1],
        color=colors_local[1],
        marker=markers_local[1],
        markersize=ms,
        mew=1,
        ls="none",
        mec="dimgrey",
        mfc=colors_local[1],
        alpha=1,
    )
    ax.plot(
        gamma[::per_data],
        period3[::per_data],
        label=labels_local[2],
        color=colors_local[2],
        marker=markers_local[2],
        markersize=ms,
        mew=1,
        ls="none",
        mec="dimgrey",
        mfc=colors_local[2],
        alpha=1,
    )

    ax.set_xlim([0, 0.82])
    ax.set_ylim([-0.04, 1.15])
    ax.set_yticks([0, 0.5, 1])
    ax.set_yticklabels([r"$0$", "", r"$1$"])
    ax.set_xticks([0, 0.4, 0.8])
    ax.set_xticklabels([r"$0$", r"$0.4$", r"$0.8$"])
    ax.set_ylabel(r"$\tilde{T}_{\mathrm{trap}}$", fontsize=fontsize, labelpad=0)

    ax.annotate(
        "total",
        fontsize=legend_fontsize + 2,
        xy=(0.62, 0.77),
        xytext=(0.67, 0.85),
        arrowprops=dict(arrowstyle="<-", color="k", lw=1.5, shrinkA=0, shrinkB=0),
    )

    ax.minorticks_off()
    ax.legend(
        ncol=3,
        columnspacing=0.5,
        fontsize=legend_fontsize - 1,
        handletextpad=0.6,
        edgecolor="k",
        labelspacing=0.4,
        handlelength=0.5,
    )

    ax.text(0.3, -0.01, r"$\gamma_s$", fontsize=fontsize, color="r")
    ax.text(0.59, 0.06, r"$\gamma_l$", fontsize=fontsize, color="b")
    ax.vlines(0.27, -0.1, 0.64, ls="--", lw=2.5, color="r", alpha=0.8)
    ax.vlines(0.67, -0.1, 0.45, ls="--", lw=2.5, color="b", alpha=0.8)

    fig.subplots_adjust(left=0.18, bottom=0.17, right=0.95, top=0.93)

    if save_bool:
        save_path = ROOT / "figure4" / "fig4a.png"
        plt.savefig(save_path, dpi=300)
    else:
        plt.show()


if __name__ == "__main__":
    save_bool = True
    plot_fig4a()