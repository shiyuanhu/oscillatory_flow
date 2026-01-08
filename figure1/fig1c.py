# Plot script for figure 1c.

import matplotlib.pyplot as plt
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from paperfig import *


def fig1c_xc_with_mag():
    setup_style(fontsize=22, font="Helvetica", usetex="auto", axes_lw=1.0, lines_lw=0.1, tick_size=5.0)

    fig, ax = plt.subplots(figsize=(5, 4), dpi=150)

    data_path = ROOT / "figure1" / "data_fig1c"
    steady = np.loadtxt(data_path / "xc_steady.txt", delimiter=",", skiprows=1)
    osc    = np.loadtxt(data_path / "xc_vortex.txt", delimiter=",", skiprows=1)
    mag    = np.loadtxt(data_path / "xc_magnet.txt", delimiter=",", skiprows=1)

    colors = ["Black", "Red", "Gray"]
    linestyle = ["-", "-", "dashed"]
    lw = 2.5

    line_steady, = ax.plot(steady[:, 0], steady[:, 1], lw=lw, color=colors[0], ls=linestyle[0], label=r"$A=0$")
    line_osc,    = ax.plot(osc[:, 0],    osc[:, 1],    lw=lw, color=colors[1], ls=linestyle[1], label=r"$A=1/2 \ W$")
    ax.plot(mag[:, 0], mag[:, 1], lw=lw, color=colors[2], ls=linestyle[2])

    # annotations 
    ax.annotate(
        r"$\mathrm{magnet}$",
        xy=(mag[36, 0], mag[36, 1] - 0.02),
        xytext=(2 / 2.33, 0.1), 
        fontsize=21,
        color="Black",
        arrowprops=dict(arrowstyle="<-", color="Black", lw=lw - 0.5),
    )

    ax.annotate(
        r"$\mathrm{vortex}$",
        xy=(osc[7, 0] + 0.1 / 2.33, osc[7, 1] + 0.02),
        xytext=(0.9 / 2.33, 0.75),
        fontsize=21,
        color="Black",
        arrowprops=dict(arrowstyle="<-", color="Black", lw=lw - 0.5),
    )

    ax.annotate(
        r"$\mathrm{vortex}$",
        xy=(0.65, 0.54),
        xytext=(0.9 / 2.33, 0.75),
        fontsize=21,
        color="Black",
        arrowprops=dict(arrowstyle="<-", color="Black", lw=lw - 0.5),
    )

    ax.set_yticks([0, 0.5, 1])
    ax.set_xticks([0, 1, 2])
    ax.set_yticklabels([r"$0$", r"$0.5$", r"$1.0$"])
    ax.set_xlim([0, 2.15])
    ax.set_ylim([0, 1])
    ax.set_ylabel(r"$x_{\mathrm{c}}/W$", labelpad=1)
    ax.set_xlabel(r"$t/\tau_0$", labelpad=0)

    ax.legend(
        handles=[line_steady, line_osc],
        loc="lower center",
        bbox_to_anchor=(0.77, 0.68),
        ncols=1,
        frameon=False,
        handletextpad=0.5,
        handlelength=1,
        columnspacing=1.5,
        fontsize=16,
        labelspacing=0.5,
        edgecolor="k",
    )

    fig.subplots_adjust(left=0.15, bottom=0.165, top=0.89, right=0.92)

    if save_bool:
        save_path = ROOT / "figure1" / "fig1c.png"
        plt.savefig(save_path, dpi=300)
    else:
        plt.show()


if __name__ == "__main__":
    save_bool = True
    fig1c_xc_with_mag()