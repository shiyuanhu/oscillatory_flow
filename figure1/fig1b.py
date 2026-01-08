# Plot script for figure 1b.

import matplotlib as mpl
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT))
from paperfig import *


def fig1b_unitcell():
    setup_style(fontsize=22, font="Helvetica", usetex="auto", axes_lw=1.0, lines_lw=0.1, tick_size=5.0)

    fig, ax = plt.subplots(figsize=(4, 4))

    data_path = ROOT / "figure1" / "data_fig1b"
    vort = np.loadtxt(data_path / "vort_grid.txt", delimiter=",", skiprows=1)
    qv   = np.loadtxt(data_path / "quiver_grid.txt", delimiter=",", skiprows=1)

    Xi, Yi, Vi = vort[:, 0], vort[:, 1], vort[:, 2]
    X, Y, U, V = qv[:, 0], qv[:, 1], qv[:, 2], qv[:, 3]

    xi = np.unique(Xi); yi = np.unique(Yi)
    Xi2, Yi2 = np.meshgrid(xi, yi)
    Vi2 = Vi.reshape(len(yi), len(xi))

    xq = np.unique(X); yq = np.unique(Y)
    X2, Y2 = np.meshgrid(xq, yq)
    U2 = U.reshape(len(yq), len(xq))
    V2 = V.reshape(len(yq), len(xq))

    ax.set_xlabel(r"$x/W$", labelpad=0)
    ax.set_ylabel(r"$y/W$", labelpad=-8)
    ax.set_ylim([-1, 1]); ax.set_yticks([-1, 0, 1])
    ax.set_xlim([-1, 1]); ax.set_xticks([-1, 0, 1])

    norm = mcolors.Normalize(vmin=-6, vmax=6)
    mesh = ax.pcolormesh(Xi2, Yi2, Vi2, norm=norm, cmap="RdBu_r", shading="auto", rasterized=True)

    ax.quiver(X2, Y2, U2, V2, scale=3, scale_units="xy", angles="xy",
              color="k", alpha=0.8, width=0.004)

    # plot different magnets
    radius = 0.4
    positions = [(0, 0.5), (0, -0.5), (-1, 0.5), (-1, -0.5), (1, 0.5), (1, -0.5)]
    alpha_m = 0.4
    label = [r"$\mathbf{N}$", r"$\mathbf{S}$", r"$\mathbf{S}$", r"$\mathbf{N}$", r"$\mathbf{S}$", r"$\mathbf{N}$"]

    for i, pos in enumerate(positions):
        circle = patches.Circle(pos, radius, edgecolor="black", facecolor="none", lw=1, alpha=alpha_m + 0.5)
        ax.add_patch(circle)
        ax.text(
            pos[0],
            pos[1] + 0.11 - 0.5 * radius,
            label[i],
            ha="center",
            fontsize=20,
            color="k",
            alpha=alpha_m + 0.6,
            clip_on=True,
            zorder=10,
        )

    cb_ax = fig.add_axes([0.365, 0.89, 0.48, 0.025])
    cbar = fig.colorbar(mesh, cax=cb_ax, orientation="horizontal")
    cbar.set_ticks([-5, 0, 5])
    cbar.ax.tick_params(labelsize=22 - 4, pad=0)
    cbar.ax.xaxis.set_ticks_position("top")
    cbar.ax.xaxis.set_label_position("top")
    cbar.ax.text(
        -0.21, -0.1,
        r"$\omega \ \mathrm{(\tau_0^{-1})}$",
        fontsize=22 - 6,
        ha="center", va="bottom",
        transform=cbar.ax.transAxes,
    )

    ax.set_aspect(1)
    fig.subplots_adjust(left=0.12, bottom=0.205)
    
    if save_bool:
        save_path = ROOT / "figure1" / "fig1b.png"
        plt.savefig(save_path, dpi=300)
    else:
        plt.show()

if __name__ == "__main__":
    save_bool = True
    fig1b_unitcell()