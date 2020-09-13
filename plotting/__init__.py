from .sweden_line_graph import plot_graph

from pathlib import Path
from . import __path__ as _dir_nspath

__all__ = ["plot_graph"]

dir_path = Path(list(_dir_nspath)[0])
