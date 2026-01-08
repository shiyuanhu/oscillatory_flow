# Plot script for figure 1d.

import matplotlib.pyplot as plt
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from paperfig import *


def fig1d_fiber_traj():
    """Fig 1d: CoM trajectories of short and long fibers"""
    setup_style(fontsize=22, font="Helvetica", usetex="auto", axes_lw=1.0, lines_lw=0.1, tick_size=5.0)

    fig, ax = plt.subplots(figsize=(4.5, 4), dpi=150)

    data_path = ROOT / "figure1" / "data_fig1d"
    short_xy = np.loadtxt(data_path / "traj_short_xy.txt", delimiter=",", skiprows=1)
    long_xy  = np.loadtxt(data_path / "traj_long_xy.txt",  delimiter=",", skiprows=1)

    ax.plot(short_xy[:, 0], short_xy[:, 1], ls="-", lw=1.5, color="red",  label=r"$\mathrm{short}$")
    ax.plot(long_xy[:, 0],  long_xy[:, 1],  ls="-", lw=1.5, color="blue", alpha=0.9, label=r"$\mathrm{long}$")

    ax.set_xlim([0.8, 9.5])
    ax.set_ylim([0.8, 9])
    ax.set_xticks([2, 8])
    ax.set_yticks([2, 8])
    ax.set_xlabel(r"$x/W$", labelpad=0)
    ax.set_ylabel(r"$y/W$", labelpad=10)
    ax.set_aspect("equal")
    ax.legend(ncol=1, bbox_to_anchor=(0.55, 1), fontsize=18, frameon=False, handlelength=1, labelspacing=0.5)
    fig.subplots_adjust(left=0.2, bottom=0.145, top=0.84, right=0.915)

    if save_bool:
        save_path = ROOT / "figure1" / "fig1d.png"
        plt.savefig(save_path, dpi=300)
    else:
        plt.show()


if __name__ == "__main__":
    save_bool = True
    fig1d_fiber_traj()