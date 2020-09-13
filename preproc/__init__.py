from .preprocess_UN_monthly_stats_all_countries import all_countries_out_prefix
from .preprocess_UN_monthly_stats_sweden import swed_out_prefix
from .preprocess_UN_population_sweden import swed_out_prefix as swed_pop_out_prefix
from pathlib import Path
from . import __path__ as _dir_nspath

__all__ = ["all_countries_out_prefix", "swed_out_prefix"]

dir_path = Path(list(_dir_nspath)[0])
