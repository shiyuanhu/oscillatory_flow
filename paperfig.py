# Style setup for matplotlib figures.
import os
import shutil
import warnings
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from typing import Iterable, Optional, Sequence, Union, Dict, List, Tuple, Any
from matplotlib.text import Text
from matplotlib.font_manager import FontProperties
from matplotlib.font_manager import FontProperties

# Path for compile latex (macOS MacTeX).
_TEXBIN_MACOS = "/Library/TeX/texbin"

# ----------------------------
# Style
# ----------------------------
def setup_style(
    *,
    fontsize: int = 20,
    font: str = "Helvetica",
    usetex: Union[bool, str] = "auto",
    axes_lw: float = 1.0,
    lines_lw: float = 0.5,
    tick_size: float = 5.0,
    latex_preamble: str = r"\usepackage{xcolor}",
    add_tex_path: bool = True,
) -> None:
    """Apply your standard paper style. If usetex="auto", use LaTeX only when available."""
    if add_tex_path and os.path.isdir(_TEXBIN_MACOS):
        os.environ["PATH"] += os.pathsep + _TEXBIN_MACOS

    if usetex == "auto":
        usetex = shutil.which("latex") is not None
    elif usetex is True and shutil.which("latex") is None:
        usetex = False
        warnings.warn("LaTeX not found -> text.usetex=False", RuntimeWarning)

    plt.rcParams.update(
        {
            "axes.labelsize": fontsize,
            "xtick.labelsize": fontsize,
            "ytick.labelsize": fontsize,
            "text.usetex": bool(usetex),
            "font.family": "sans-serif",
            "font.sans-serif": [font],
            "xtick.direction": "in",
            "ytick.direction": "in",
            "xtick.major.size": tick_size,
            "ytick.major.size": tick_size,
            "axes.linewidth": axes_lw,
            "lines.linewidth": lines_lw,
        }
    )

    if bool(usetex) and latex_preamble:
        plt.rcParams["text.latex.preamble"] = latex_preamble
