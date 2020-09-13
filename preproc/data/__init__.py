from pathlib import Path
from . import __path__ as _dir_nspath

__all__ = []

dir_path = Path(list(_dir_nspath)[0])
