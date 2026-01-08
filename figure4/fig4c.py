# Plot script for figure 4c.

import matplotlib.pyplot as plt
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from paperfig import *
from matplotlib.patches import FancyArrowPatch


def plot_fig4c():
    # ----------------------------
    # Settings 
    # ----------------------------
    fontsize = 19
    ms = 7
    mew = 1
    lw = 1.2
    cap = 3
    left, bottom = 0.1, 0.2
    top = 0.93

    setup_style(
        fontsize=fontsize,
        font="Helvetica",
        usetex="auto",
        axes_lw=1.0,
        lines_lw=0.1,
        tick_size=5.0,
    )

    fig, ax = plt.subplots(figsize=(4, 4.0), dpi=150)

    data_dir = ROOT / "figure4" / "data_fig4c"

    # ----------------------------
    # Load final exported data
    # ----------------------------
    nu_file = data_dir / "alpha_gamma.txt"
    traj_sub_file = data_dir / "traj_gamma_0.40.txt"
    traj_diff_file = data_dir / "traj_gamma_0.80.txt"

    data = np.loadtxt(nu_file, delimiter=",", skiprows=1)
    data_sub = np.loadtxt(traj_sub_file, delimiter=",", skiprows=1)
    data_diff = np.loadtxt(traj_diff_file, delimiter=",", skiprows=1)

    # main curve
    ax.errorbar(
        data[:, 0], data[:, 1], data[:, 2],
        ls="none", mew=mew, mfc="none", color="k",
        marker="o", markersize=ms,
        linewidth=lw, capsize=cap, alpha=0.8
    )

    idx_sub = np.where(np.isclose(data[:, 0], 0.4))[0]
    idx_diff = np.where(np.isclose(data[:, 0], 0.8))[0]

    ax.errorbar(
        data[idx_sub, 0], data[idx_sub, 1], data[idx_sub, 2],
        ls="none", mec="dimgrey", marker="o", color="limegreen",
        markersize=ms, linewidth=max(lw - 0.5, 0.5), capsize=cap, alpha=1, zorder=10
    )
    ax.errorbar(
        data[idx_diff, 0], data[idx_diff, 1], data[idx_diff, 2],
        ls="none", mec="dimgrey", marker="o", color="limegreen",
        markersize=ms, linewidth=max(lw - 0.5, 0.5), capsize=cap, alpha=1, zorder=10
    )

    ax.set_xlabel(r"$\gamma$", fontsize=fontsize, labelpad=-5)
    ax.set_ylabel(r"$\alpha$", fontsize=fontsize, labelpad=10, rotation=0, va="center")

    inset_line_color = "#4A4A4A"
    axis_bool = "off"

    # -----------------
    # Insets 
    # -----------------
    sub_ax1 = ax.inset_axes([0.145, 0.63, 0.32, 0.32])
    sub_ax1.set_aspect(1)
    sub_ax1.plot(data_sub[:, 0], data_sub[:, 1], lw=0.5, color=inset_line_color)
    sub_ax1.axis(axis_bool)

    dis1 = 0.7
    arrow1 = FancyArrowPatch(
        (np.min(data_sub[:, 0]), np.min(data_sub[:, 1]) - dis1),
        (np.max(data_sub[:, 0]), np.min(data_sub[:, 1]) - dis1),
        arrowstyle="<->", mutation_scale=16, color=inset_line_color
    )
    sub_ax1.add_patch(arrow1)
    sub_ax1.set_ylim(-4, 1.1)

    sub_ax2 = ax.inset_axes([0.46, 0.06, 0.5, 0.5])
    sub_ax2.set_aspect(1)
    sub_ax2.plot(data_diff[:, 0], data_diff[:, 1], lw=0.5, color=inset_line_color)
    sub_ax2.axis(axis_bool)

    dis2 = 2
    arrow2 = FancyArrowPatch(
        (np.min(data_diff[:, 0]), np.min(data_diff[:, 1]) - dis2),
        (np.max(data_diff[:, 0]), np.min(data_diff[:, 1]) - dis2),
        arrowstyle="<->", mutation_scale=16, color=inset_line_color
    )
    sub_ax2.add_patch(arrow2)
    sub_ax2.set_ylim(-18, 20)

    # texts
    ax.text(0.2, 0.7, r"$7 \ W$", fontsize=fontsize - 4, color=inset_line_color)
    ax.text(0.54, -0.02, r"$32 \ W$", fontsize=fontsize - 4, color=inset_line_color)
    ax.text(0.15, 1.01, r"$\gamma = 0.4$", fontsize=fontsize - 3, color="green")
    ax.text(0.48, 0.61, r"$\gamma = 0.8$", fontsize=fontsize - 3, color="green")

    # ticks/limits
    ax.set_xticks([0, 0.2, 0.4, 0.6, 0.8])
    ax.set_yticks([0, 0.5, 1])
    ax.set_yticklabels([r"$0$", "", r"$1$"])
    ax.set_xticklabels([r"$0$", "", r"$0.4$", "", r"$0.8$"])
    ax.set_xlim([-0.015, 0.84])
    ax.set_ylim([-0.04, 1.09])

    # special markers
    ax.vlines(0.25, -0.1, 0.4, ls="--", lw=2.5, color="r", alpha=0.8)
    ax.vlines(0.72, 0.4, 1.2, ls="--", lw=2.5, color="b", alpha=0.8)

    ax_top = ax.secondary_xaxis("top")
    ax_top.set_xticks([0, 0.2, 0.4, 0.6, 0.8])
    ax_top.set_xticklabels([])

    ax.text(0.31, 0.0, r"$\gamma_s$", color="r", fontsize=fontsize)
    ax.text(0.64, 1.02, r"$\gamma_l$", color="b", fontsize=fontsize)

    fig.subplots_adjust(left=left, bottom=bottom, top=top, right=0.95)

    if save_bool:
        save_path = ROOT / "figure4" / "fig4c.png"
        plt.savefig(save_path, dpi=300)
    else:
        plt.show()


if __name__ == "__main__":
    save_bool = True
    plot_fig4c()